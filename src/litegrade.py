#!/home/jmorga27/Cal_Poly/Kurfess/litegrade/bin/python3

# litegrade.py 
#   This script contains student-interfacing functions that can be seen at the 
#   notebook level

import json

from importlib import reload
import modulemanager
modulemanager = reload(modulemanager)
from modulemanager import print_err, safe_fopen, hello_from_qdriver

def load_questions(json_fname):

	questions_fobj = safe_fopen("questions.json", 'r')

	try:
		questions_obj = json.load(questions_fobj)
	except OSError as err:
		print_err(f"{msg_prefix}: '{fname}' json load error")
		print_err(f"(OS error below)\n{err}", callback=lambda: exit(1))

	return questions_obj

def get_input(msg, valid_inputs_list):
	user_input = input(msg)
	while not user_input:
		print("  Please enter something")
		user_input = input(msg)
	
	if not valid_inputs_list:
		return user_input

	while user_input not in valid_inputs_list:
		print(f"  '{user_input}' is not a valid input")
		print(f"  valid inputs include {valid_inputs_list}")
		user_input = input(msg)

	return user_input

def mutate_question(questions_obj):
	hello_from_qdriver({},[questions_obj])

def hello_from_litegrade():
	print("hello from litegrade function")

def init_student(assignment_name):
	print("Please enter your name below")
	first_name = get_input("First Name: ", [])
	last_name = get_input("Last Name: ", ["a", "b"])
	id_number = "" #input("ID Number: ")
	student_obj = {
		"name": {
			"first": first_name,
			"last": last_name},
		"id": id_number,
		"assignment": assignment_name, #questions_obj}#init_assignment(assignment_name)}
		"questions": []
	}
	return student_obj

def begin(assignment_name):
	student_obj = init_student(assignment_name)
	return student_obj





