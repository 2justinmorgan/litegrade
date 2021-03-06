
# questiondriver.py 
#   This script reads a given questions dictionary/object to get info about 
#   a particular question

import json

from .commondriver import \
	print_err, \
	safe_fopen

def get_nested_value(nested_keys_and_indices_list, val_obj_or_list):

	if len(nested_keys_and_indices_list) <= 0:
		return val_obj_or_list
	
	first_key_or_index = nested_keys_and_indices_list[0]

	if type(val_obj_or_list) == list:
		list_ = val_obj_or_list

		if type(first_key_or_index) != int:
			return None
		index = first_key_or_index

		if index <= 0 or index >= len(val_obj_or_list):
			return None

		return get_nested_value(nested_keys_and_indices_list[1:], list_[index])
	
	if type(val_obj_or_list) == dict:
		new_val_obj_or_list = val_obj_or_list.get(first_key_or_index, {})
		return get_nested_value( \
			nested_keys_and_indices_list[1:], \
			new_val_obj_or_list)

	# returns either a string or number (this is a result of misusing this func)
	return val_obj_or_list
	
def hello_from_qdriver(obj, *argv):
	if len(argv) > 0:
		questions_obj = argv[0][0]
		nested_keys_and_indices_arr = \
			["questions","gravy_question","choices",1]
		answer_choice = \
			get_nested_value(nested_keys_and_indices_arr, questions_obj)
		answer_choice.update(description = "NEW Answer Description")
		return
	nested_element = get_nested_value(["keyB",1], obj)
	nested_element.update(key_BB = "New value added")
	
def load_questions(json_fname):

	questions_fobj = safe_fopen("questions.json", 'r')

	try:
		questions_obj = json.load(questions_fobj)
	except OSError as err:
		print_err(f"{msg_prefix}: '{fname}' json load error")
		print_err(f"(OS error below)\n{err}", callback=lambda: exit(1))

	return questions_obj

def record_answer(question_name, answer_str, answers_obj):
	answers_lst = answers_obj.get(question_name, [])
	answers_lst.append(answer_str)
	answers_obj[question_name] = answers_lst


