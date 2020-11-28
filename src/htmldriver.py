
# htmldriver.py
#   This script creates and edits string representations of html elements
#   that will later be rendered and displayed via IPython

from .questiondriver import \
	load_questions, \
	get_nested_value

ENV_JS = {
	"standard-ipynb": """
		initializeCmd = 'if "litegrade" not in globals(): import litegrade';
		IPython.notebook.kernel.execute(initializeCmd);
		ans = selections;
		ansO = 'litegrade.answers_obj';
		cmd = 'litegrade.record_answer("{question_name}","'+ans+'",'+ansO+')';
		IPython.notebook.kernel.execute(cmd);
	""",
	"google-colab": """
		google.colab.kernel.invokeFunction('{question_name}-id', [], {{}});
		lgAns = selections;
	"""
}

def create_node(tag_str, attributes_obj, inner_text_str):
	node = f"<{tag_str}"
	for attribute_name in attributes_obj:
		attribute_value = attributes_obj.get(attribute_name,"")
		node += f" {attribute_name}=\"{attribute_value}\""
	node += f">{inner_text_str}</{tag_str}>"
	return node
	
def create_question_choices_nodes( \
	label_type_str, choices_attributes_obj, choices_lst):
	choices = ""
	choice_num = 0
	for choice_str in choices_lst:
		choice_num += 1
		choice_num_str = "choice-" + str(choice_num)
		input_attributes_obj = {
			"id": choice_num_str,
			"type": label_type_str,
			"name": "choice"
		}
		label_attributes_obj = { "for": choice_num_str }
		choices += create_node("input",input_attributes_obj,"")
		choices += create_node("label",label_attributes_obj,choice_str)
		choices += "<br>"
	return choices

def create_question_node( \
	question_name_str, prompt_str, label_type_str, choices_lst):

	# question prompt node
	prompt_node = create_node("div",{"class":"question-prompt"},prompt_str)

	# question choices
	inner_nodes = create_question_choices_nodes(label_type_str,{},choices_lst)
	choices_node = create_node("div",{"class":"question-choices"},inner_nodes)

	# submit button
	submit_button = create_node( \
		"button", \
		{"class":"submit-button","type":"submit","qname":question_name_str}, \
		"Submit")

	# insert innerHTML into question_node
	question_node_inner_html = prompt_node + choices_node + submit_button
	question_node = create_node( \
		"div", \
		{"id":question_name_str,"class":"question-node"}, \
		question_node_inner_html)

	return question_node

def get_javascript(question_name, notebook_environment):
	javascript = """
		<script type="text/Javascript">
			if (typeof qNodes === 'undefined')  qNodes = {{}};
			if (typeof sButtons === 'undefined') sButtons = {{}};
			if (typeof cNodes === 'undefined') cNodes = {{}};
			qName = "{question_name}";
			qNodes[qName] = document.querySelector('#'+qName);
			cNodes[qName] = qNodes[qName].querySelector(".question-choices");
			sButtons[qName] = qNodes[qName]
				.querySelector('button[qname="'+qName+'"]');
			sButtons[qName].onclick = e => {{
				thisqName = e.target.getAttribute("qname");
				inputs = cNodes[thisqName].querySelectorAll("input");
				// concatenation of all selected answers upon clicking "Submit"
				selections = "";
				for (var i=0; i<inputs.length; i++) {{
					var label =
						cNodes[thisqName]
							.querySelector("label[for='"+inputs[i].id+"']");
					if (inputs[i].checked)
						selections += label.innerText + " | ";
				}}
				// remove trailing " | "
				selections = selections.slice(0,-3);
				{env_specific_javascript}
			}}
		</script>
		"""
	javascript = javascript.format( \
		question_name = question_name, \
		env_specific_javascript = \
			ENV_JS[notebook_environment].format(question_name = question_name))

	return javascript

def get_html(question_name):
	questions_obj = load_questions("questions.json")
	question_obj = get_nested_value(["questions",question_name],questions_obj)

	prompt_str = get_nested_value(["prompt"], question_obj)
	label_type_str = get_nested_value(["choices_label_type"], question_obj)
	choices_obj_lst = get_nested_value(["choices"], question_obj)
	choices_lst = [o.get("description","") for o in choices_obj_lst]

	return create_question_node( \
		question_name, prompt_str, label_type_str, choices_lst)



