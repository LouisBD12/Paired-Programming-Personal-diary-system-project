'''3'''
from lib.check_to_do import *

def test_checks_for_to_do():
    assert check_to_do("#TODO") == True
    assert check_to_do("#TODO - do the dishes") == True
    assert check_to_do("do the dishes #TODO") == True

def test_checks_for_no_to_do():
    assert check_to_do("do the dishes") == False
    assert check_to_do("") == False