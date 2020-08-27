#!/home/jmorga27/Cal_Poly/Kurfess/litegrade/bin/python3

# litegrade.py 
#   This script contains student-interfacing functions that are seen at the 
#   notebook level

import os
import sys
import inspect
import json

msg_prefix = "litegrade"

def print_err(msg, **kwargs):
	frame = inspect.stack()[1]
	caller_line_num = inspect.getframeinfo(inspect.stack()[1][0]).lineno
	sys.stderr.write(f"{msg_prefix}: (line {caller_line_num}) {msg}\n")

	callback = kwargs.get("callback", None)
	if callback != None:
		callback()

def safe_fopen(fname, mode):
	if not os.path.isfile(fname):
		print_err(f"'{fname}' not found", callback=lambda: exit(1))

	try:
		fobj = open(fname, mode=mode)
	except OSError as err:
		print_err(f"'{fname}' open error")
		print_err(f"(OS error below)\n{err}", callback=lambda: exit(1))

	return fobj

def load_questions(json_fname):

	questions_fobj = safe_fopen("questions.json", 'r')

	try:
		questions_obj = json.load(questions_fobj)
	except OSError as err:
		print_err(f"{msg_prefix}: '{fname}' json load error")
		print_err(f"(OS error below)\n{err}", callback=lambda: exit(1))

	return questions_obj




