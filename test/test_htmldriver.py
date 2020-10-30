import pytest
import htmldriver
import importlib
 
@pytest.fixture(autouse=True)
def before_each():
	import htmldriver
	htmldriver = importlib.reload(htmldriver)

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
	assert expect == \
		htmldriver.create_node(tag_str, attributes_obj, inner_text_str)

@pytest.mark.parametrize(
	"label_type_str,choices_attributes_obj,choices_lst,expect",
	[
		(
			"A",
			{},
			["choice1","choice2","choice3"],
			('<ol type="A">'
				'<li id="choice-1">'
					'choice1'
				'</li>'
				'<li id="choice-2">'
					'choice2'
				'</li>'
				'<li id="choice-3">'
					'choice3'
				'</li>'
			'</ol>')),
		(
			"i",
			{"class":"some-class","style":"background:yellow;"},
			["True","False"],
			('<ol type="i">'
				'<li class="some-class" style="background:yellow;" id="choice-1">'
					'True'
				'</li>'
				'<li class="some-class" style="background:yellow;" id="choice-2">'
					'False'
				'</li>'
			'</ol>'))
	])
def test_create_question_choices_nodes( \
	label_type_str, choices_attributes_obj, choices_lst, expect):
	assert expect == \
		htmldriver.create_question_choices_nodes( \
			label_type_str, choices_attributes_obj, choices_lst)

@pytest.mark.parametrize(
	"question_name_str,prompt_str,label_type_str,choices_lst,expect",
	[
		(
			"this_question_name",
			"This prompt is funny",
			"i",
			["True","False"],
			('<div id="this_question_name" class="question-node">'
				'<div class="question-prompt">'
					'This prompt is funny'
				'</div>'
				'<div class="question-choices">'
					'<ol type="i">'
						'<li id="choice-1" class="choice">'
							'True'
						'</li>'
						'<li id="choice-2" class="choice">'
							'False'
						'</li>'
					'</ol>'
				'</div>'
			'</div>')),
		(
			"sample_question_name",
			"This is a prompt",
			"a",
			["Sure","Yeah man","OK","All the above"],
			('<div id="sample_question_name" class="question-node">'
				'<div class="question-prompt">'
					'This is a prompt'
				'</div>'
				'<div class="question-choices">'
					'<ol type="a">'
						'<li id="choice-1" class="choice">'
							'Sure'
						'</li>'
						'<li id="choice-2" class="choice">'
							'Yeah man'
						'</li>'
						'<li id="choice-3" class="choice">'
							'OK'
						'</li>'
						'<li id="choice-4" class="choice">'
							'All the above'
						'</li>'
					'</ol>'
				'</div>'
			'</div>'))
	])
def test_create_question_node( \
	question_name_str, prompt_str, label_type_str, choices_lst, expect):
	assert expect == \
		htmldriver.create_question_node( \
			question_name_str, prompt_str, label_type_str, choices_lst)


