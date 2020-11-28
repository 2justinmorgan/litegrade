import pytest
import importlib
from .htmldriver import \
	create_node, \
	create_question_choices_nodes, \
	create_question_node
 
@pytest.fixture(autouse=True)
def before_each():
	from .htmldriver import \
		create_node, \
		create_question_choices_nodes, \
		create_question_node

@pytest.mark.parametrize(
	"tag_str,attributes_obj,inner_text_str,expect",
	[
		(
			"div",
			{"class":"basic","src":"http://me.com"},
			"Some inner text",
			'<div class="basic" src="http://me.com">Some inner text</div>'),
		(
			"li",
			{"style":"color:red;padding:2px;"},
			"",
			'<li style="color:red;padding:2px;"></li>')
	])
def test_create_node(tag_str, attributes_obj, inner_text_str, expect):
	assert expect == create_node(tag_str, attributes_obj, inner_text_str)

@pytest.mark.parametrize(
	"label_type_str,choices_attributes_obj,choices_lst,expect",
	[
		(
			"checkbox",
			{},
			["choice1","choice2","choice3"],
			(
				'<input id="choice-1" type="checkbox" name="choice"></input>'
				'<label for="choice-1">choice1</label>'
				'<br>'
				'<input id="choice-2" type="checkbox" name="choice"></input>'
				'<label for="choice-2">choice2</label>'
				'<br>'
				'<input id="choice-3" type="checkbox" name="choice"></input>'
				'<label for="choice-3">choice3</label>'
				'<br>')),
		(
			"radio",
			{},
			["True","False"],
			(
				'<input id="choice-1" type="radio" name="choice"></input>'
				'<label for="choice-1">True</label>'
				'<br>'
				'<input id="choice-2" type="radio" name="choice"></input>'
				'<label for="choice-2">False</label>'
				'<br>'))
	])
def test_create_question_choices_nodes( \
	label_type_str, choices_attributes_obj, choices_lst, expect):
	assert expect == \
		create_question_choices_nodes( \
			label_type_str, choices_attributes_obj, choices_lst)

@pytest.mark.parametrize(
	"question_name_str,prompt_str,label_type_str,choices_lst,expect",
	[
		(
			"this_q_name",
			"This prompt is funny",
			"radio",
			["True","False"],
			('<div id="this_q_name" class="question-node">'
				'<div class="question-prompt">'
					'This prompt is funny'
				'</div>'
				'<div class="question-choices">'
					'<input id="choice-1" type="radio" name="choice"></input>'
					'<label for="choice-1">True</label>'
					'<br>'
					'<input id="choice-2" type="radio" name="choice"></input>'
					'<label for="choice-2">False</label>'
					'<br>'
				'</div>'
				'<button class="submit-button" type="submit" qname="this_q_name">'
					'Submit'
				'</button>'
			'</div>')),
		(
			"sample_name",
			"This is a prompt",
			"checkbox",
			["Sure","Yeah man","OK","All the above"],
			('<div id="sample_name" class="question-node">'
				'<div class="question-prompt">'
					'This is a prompt'
				'</div>'
				'<div class="question-choices">'
					'<input id="choice-1" type="checkbox" name="choice"></input>'
					'<label for="choice-1">Sure</label>'
					'<br>'
					'<input id="choice-2" type="checkbox" name="choice"></input>'
					'<label for="choice-2">Yeah man</label>'
					'<br>'
					'<input id="choice-3" type="checkbox" name="choice"></input>'
					'<label for="choice-3">OK</label>'
					'<br>'
					'<input id="choice-4" type="checkbox" name="choice"></input>'
					'<label for="choice-4">All the above</label>'
					'<br>'
				'</div>'
				'<button class="submit-button" type="submit" qname="sample_name">'
					'Submit'
				'</button>'
			'</div>'))
	])
def test_create_question_node( \
	question_name_str, prompt_str, label_type_str, choices_lst, expect):
	assert expect == \
		create_question_node( \
			question_name_str, prompt_str, label_type_str, choices_lst)


