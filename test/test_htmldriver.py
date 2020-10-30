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

	
