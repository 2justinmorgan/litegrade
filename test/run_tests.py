#!/home/jmorga27/Cal_Poly/Kurfess/litegrade/bin/python3

dir_of_code_to_test = "/home/jmorga27/Cal_Poly/Kurfess/litegrade/src"

import os
import sys
sys.path.insert(1, dir_of_code_to_test)
current_dir = os.path.dirname(os.path.realpath(__file__))

import inspect
from unittesting import my_assert

from importlib import reload
import litegrade
litegrade = reload(litegrade)
from litegrade import load_questions

msg_prefix = "testing"

def print_err(msg, **kwargs):
	frame = inspect.stack()[1]
	caller_line_num = inspect.getframeinfo(inspect.stack()[1][0]).lineno
	sys.stderr.write(f"{msg_prefix}: (line {caller_line_num}) {msg}\n")

	callback = kwargs.get("callback", None)
	if callback != None:
		callback()
	
def load_questions_tests():
	questions_fname = "questions.json"
	questions_obj = {
		"questions": {
			"apples_question": {
				"question_type": "multiple-choice",
				"prompt": "How do you like them apples?",
				"choices_label_type": "letters",
				"choices": [
					{
						"description": "They're great!",
						"explanation": "Even though Matt Damon asked, the question isn't referring to apples"
					},
					{
						"description": "They're my favorite!",
						"explanation": "Though they keep the doctor away, the question isn't referring to apples"
					},
					{
						"description": "I'd rather have an orange",
						"explanation": "Though citrus is good for you, the question isn't referring to fruit"
					},
					{
						"description": "None of the above",
						"explanation": "'apples' is a metaphor"
					}
				],
				"correct_choice": 3
			},
			"gravy_question": {
				"question_type": "multiple-choice",
				"prompt": "Do you like gravy in your cereal?",
				"choices_label_type": "numbers",
				"choices": [
					{
						"description": "Obsolutely not!",
						"explanation": "Cereal tastes much better with cereal, a breakfast meal"
					},
					{
						"description": "Only on the side",
						"explanation": "Gravy on the side makes more sense. However, it's not suited for breakfast"
					},
					{
						"description": "Uhh, yeah! Gravy is my favorite",
						"explanation": "Though gravy is good, it's better suited for dinner"
					}
				],
				"correct_choice": 0
			},
			"cleverness_question": {
				"question_type": "true-or-false",
				"prompt": "Are these questions clever?",
				"correct_answer": "true",
				"explaination": "They're so good, an explaination is not needed"
			}
		}
	}

	if not os.path.isfile(questions_fname):
		print_err(f"'"+questions_fname+"' not found", callback=lambda: None)
	
	my_assert(load_questions(questions_fname), questions_obj)

def main():
	load_questions_tests()

main()




