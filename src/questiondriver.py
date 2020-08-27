#!/home/jmorga27/Cal_Poly/Kurfess/litegrade/bin/python3

# questiondriver.py 
#   This script reads a given questions dictionary/object to get info about 
#   a particular question

from importlib import reload
import commondriver
commondriver = reload(commondriver)
from commondriver import print_err

def get_nested_value(nested_keys_and_indices_arr, obj):
	
	val = obj
	for element in nested_keys_and_indices_arr:
		if type(val) == list and type(element) == int:
			index = element
			val = val[index] if index >= 0 and index < len(val) else {}
		else:
			key = element
			val = val.get(key, {})
	
	target_value = val
	return target_value
	
def hello_from_qdriver(obj):
	nested_element = get_nested_value(["keyB","key_BB"], obj)
	

