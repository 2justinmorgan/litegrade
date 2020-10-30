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


