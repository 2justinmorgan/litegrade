
# modulemanager.py 
#   This script manages all needed modules for litegrade.py, to increase 
#   organization and reduce import overhead

from importlib import reload
import commondriver
import questiondriver
commondriver = reload(commondriver)
questiondriver = reload(questiondriver)
from commondriver import print_err, safe_fopen
from questiondriver import hello_from_qdriver
