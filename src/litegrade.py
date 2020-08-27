#!/home/jmorga27/Cal_Poly/Kurfess/litegrade/bin/python3

# litegrade.py 
#   This script contains student-interfacing functions that can be seen at the 
#   notebook level

import json

from importlib import reload
import commondriver
commondriver = reload(commondriver)
from commondriver import print_err, safe_fopen

def load_questions(json_fname):

	questions_fobj = safe_fopen("questions.json", 'r')

	try:
		questions_obj = json.load(questions_fobj)
	except OSError as err:
		print_err(f"{msg_prefix}: '{fname}' json load error")
		print_err(f"(OS error below)\n{err}", callback=lambda: exit(1))

	return questions_obj




