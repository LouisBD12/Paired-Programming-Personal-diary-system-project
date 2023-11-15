from lib.improve_grammar import *

def test_improved_grammar():
    assert check_grammar("The cow jumped over the moon.") == True
    assert check_grammar("The cow jumped over the moon?") == True
    assert check_grammar("The cow jumped over the moon!") == True
def test_bad_grammar():
    assert check_grammar("the cow jumped over the moon.") == False
    assert check_grammar("The cow jumped over the moon") == False
    assert check_grammar("the cow jumped over the moon") == False

