from lib.manage_time import *

def test_words_is_10000():
    assert reading_time(10000) == "50 minutes"

def test_words_is_150():
    assert reading_time(150) == "0.75 minutes"

def test_words_is_500():
    assert reading_time(500) == "2.5 minutes"
