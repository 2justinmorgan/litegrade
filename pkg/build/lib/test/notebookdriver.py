
# litegrade.py 
#   This script contains student-interfacing functions that can be seen at the 
#   notebook level

from .commondriver import get_notebook_env
from .questiondriver import hello_from_qdriver
from .questiondriver import record_answer
from .htmldriver import get_html
from .htmldriver import get_javascript
from IPython.display import HTML, display

ENV = get_notebook_env()
answers_obj = {}

def mutate_question(questions_obj):
	hello_from_qdriver({},[questions_obj])

def ask(question_name):

	html_str = get_html(question_name)
	javascript_str = get_javascript(question_name, ENV)
	display(HTML(html_str + javascript_str))

	# register js-to-py callback for Google Colab notebooks
	if ENV == "google-colab":
		from google.colab.output import register_callback, eval_js
		register_callback( \
			question_name+"-id", \
			lambda: record_answer(question_name, eval_js('lgAns'), answers_obj))

