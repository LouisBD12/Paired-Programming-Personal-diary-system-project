import pytest 
from lib.personal_diary_system import *

def test_make_snippet_over_five_words():
    assert make_snippet("Today I went to the park and saw someone holding an ice cream") == "Today I went to the..."

    
def test_make_snippet_equals_5_words():
    assert make_snippet("Tomorrow is cinema time") == "Tomorrow is cinema time"

def test_make_snippet_under_5_words():
    assert make_snippet("Hello") == "Hello"

def test_length_of_words_is_3():
    assert count_words("I am person") == 3

def test_length_of_words_is_5():
    assert count_words("Hello I am person bye") == 5

def test_length_of_words_is_8():
    assert count_words("I went to the shops and bought crisps") == 8
