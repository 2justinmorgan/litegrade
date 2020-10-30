
# htmldriver.py
#   This script creates and edits string representations of html elements
#   that will later be rendered and displayed via IPython

def create_node(tag_str, attributes_obj, inner_text_str):
	node = f"<{tag_str}"
	for attribute_name in attributes_obj:
		attribute_value = attributes_obj.get(attribute_name,"")
		node += f" {attribute_name}=\"{attribute_value}\""
	node += f">{inner_text_str}</{tag_str}>"
	return node
	
def create_question_choices_nodes( \
	label_type_str, choices_attributes_obj, choices_lst):
	questions = f"<ol type=\"{label_type_str}\">"
	question_num = 0
	for choice_str in choices_lst:
		question_num += 1
		question_num_str = "choice-" + str(question_num)
		choices_attributes_obj["id"] = question_num_str
		questions += create_node("li",choices_attributes_obj,choice_str)
	questions += "</ol>"
	return questions

def create_question_node( \
	question_name_str, prompt_str, label_type_str, choices_lst):

	question_node = create_node( \
		"div",{"id":question_name_str,"class":"question-node"},"")

	# add question prompt node
	question_node = question_node[:question_node.find('>')+1] + \
		create_node("div",{"class":"question-prompt"},prompt_str)

	# add question choices
	question_choices_node = \
		create_node("div",{"class":"question-choices"},"")[:-6]
	question_choices_node += create_question_choices_nodes( \
		label_type_str, {"id":"","class":"choice"},choices_lst)
	question_choices_node += "</div>"

	question_node += question_choices_node + "</div>"
	return question_node


