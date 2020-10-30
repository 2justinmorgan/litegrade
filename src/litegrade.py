
# litegrade.py 
#   This script contains student-interfacing functions that can be seen at the 
#   notebook level

from modulemanager import \
	hello_from_qdriver, \
	get_html, \
	get_javascript, \
	HTML, \
	display

def mutate_question(questions_obj):
	hello_from_qdriver({},[questions_obj])

def ask(question_name):
	html_str = get_html(question_name)
	javascript_str = get_javascript(question_name)
	display(HTML(html_str + javascript_str))

