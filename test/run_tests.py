#!/home/jmorga27/Cal_Poly/Kurfess/litegrade/bin/python3

dir_of_code_to_test = "/home/jmorga27/Cal_Poly/Kurfess/litegrade/src"

import os
import sys

#sys.path.insert(1, dir_of_code_to_test)
#current_dir = os.path.dirname(os.path.realpath(__file__))

import inspect
from unittesting import my_assert

from importlib import reload
import litegrade
import questiondriver
#import commondriver
litegrade = reload(litegrade)
questiondriver = reload(questiondriver)
#commondriver = reload(commondriver)
from litegrade import load_questions
from questiondriver import get_nested_value
#from commondriver import *

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
	expected_questions_obj = {
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
	
	my_assert(load_questions(questions_fname), expected_questions_obj)

def get_nested_value_tests():

	# def get_nested_value(nested_keys_and_indices_arr, obj):
	# return target_value

	# Test 1
	input_obj = {
		"keyA": "valA",
		"keyB": {
			"keyBA": "valBA"
		},
		"keyC": "valC"
	}
	nested_keys_and_indices_arr = ["keyB"]
	expected_value = {"keyBA": "valBA"}

	my_assert( \
		get_nested_value(nested_keys_and_indices_arr, input_obj), \
		expected_value)

	# Test 2
	input_obj = {
		"keyA": "valA",
		"keyB": {
			"keyBA": "valBA"
		},
		"keyC": "valC"
	}
	nested_keys_and_indices_arr = ["keyB", "keyBA"]
	expected_value = "valBA"

	my_assert( \
		get_nested_value(nested_keys_and_indices_arr, input_obj), \
		expected_value)

	# Test 3
	input_obj = {
		"keyA": "valA",
		"keyB": {
			"keyBA": "valBA"
		},
		"keyC": {
			"keyCA": {
				"keyCAA": "valCAA",
				"keyCAB": [2, 5, 4]
			}
		}
	}
	nested_keys_and_indices_arr = ["keyC", "keyCA", "keyCAB"]
	expected_value = [2, 5, 4]

	my_assert( \
		get_nested_value(nested_keys_and_indices_arr, input_obj), \
		expected_value)

	# Test 4
	input_obj = {
		"keyA": "valA",
		"keyB": {
			"keyBA": "valBA"
		},
		"keyC": {
			"keyCA": {
				"keyCAA": "valCAA",
				"keyCAB": [2, 5, 4]
			}
		}
	}
	nested_keys_and_indices_arr = []
	expected_value = input_obj

	my_assert( \
		get_nested_value(nested_keys_and_indices_arr, input_obj), \
		expected_value)

	# Test 5
	input_obj = {
		"keyA": "valA",
		"keyB": {
			"keyBA": "valBA"
		},
		"keyC": {
			"keyCA": {
				"keyCAA": "valCAA",
				"keyCAB": [2, 5, 4]
			}
		}
	}
	nested_keys_and_indices_arr = ["keyC", "keyCD", "keyCAA"]
	expected_value = {}

	my_assert( \
		get_nested_value(nested_keys_and_indices_arr, input_obj), \
		expected_value)

	# Test 6
	input_obj = {
		"keyA": "valA",
		"keyB": {
			"keyBA": "valBA"
		},
		"keyC": {
			"keyCA": [
				{
					"keyCAA": "valCAA"
				},
				{
					"keyCAB": [8, 3, 9]
				}
			]
		}
	}
	nested_keys_and_indices_arr = ["keyC", "keyCA", 1 ,"keyCAB"]
	expected_value = [8, 3, 9]

	my_assert( \
		get_nested_value(nested_keys_and_indices_arr, input_obj), \
		expected_value)

	# Test 7
	input_obj = {
		"keyA": "valA",
		"keyB": {
			"keyBA": "valBA"
		},
		"keyC": {
			"keyCA": [
				{
					"keyCAA": "valCAA"
				},
				{
					"keyCAB": [8, 3, 9]
				}
			]
		}
	}
	nested_keys_and_indices_arr = ["keyC", "keyCA", 1 ,"keyCAZ"]
	expected_value = {}

	my_assert( \
		get_nested_value(nested_keys_and_indices_arr, input_obj), \
		expected_value)

def main():
	load_questions_tests()
	get_nested_value_tests()

main()




