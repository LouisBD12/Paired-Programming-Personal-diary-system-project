import pytest
from lib.diary import *

'''initially, we should have an empty lift of entries'''

def test_initially_empty_list():
    diary = Diary()
    assert diary.all() == []

'''initially, word count is zero'''

def test_word_count_is_zero():
    diary = Diary()
    assert diary.count_words() == 0

'''initially, reading_time should '''

def test_initially_reading_time_raises_an_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == "No entries added yet"