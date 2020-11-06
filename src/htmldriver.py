
# htmldriver.py
#   This script creates and edits string representations of html elements
#   that will later be rendered and displayed via IPython

from modulemanager import \
	load_questions, \
	get_nested_value

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




	return question_node

def get_javascript(question_name, notebook_environment):
	javascript = """
		<script type="text/Javascript">
			document.querySelector("#{question_name} > .question-choices")
				.onclick = e => {{
		"""

	# insert environment-specific JavaScript code for onclick event func body
	if notebook_environment == "standard-ipynb":
		javascript += """
			initializeCmd = 'if "litegrade" not in globals(): import litegrade';
			IPython.notebook.kernel.execute(initializeCmd);
			ans = e.target.innerText;
			ansO = 'litegrade.answers_obj';
			cmd = 'litegrade.record_answer("{question_name}","'+ans+'",'+ansO+')';
			IPython.notebook.kernel.execute(cmd);
		"""
	if notebook_environment == "google-colab":
		javascript += """
			google.colab.kernel.invokeFunction('{question_name}-id', [], {{}});
			lgAns = e.target.innerText;
		"""

	javascript += """
				}};
		</script>
	"""
	javascript = javascript.format(question_name = question_name)
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


