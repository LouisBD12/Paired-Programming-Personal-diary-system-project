from lib.diary_entry import *

'''when i initialise with a title and contents
i can get that title and contents back'''

def test_contructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

'''when i initialise a five word contents
then count_words should return the int 5.'''

def test_five_word_contents():
    diary_entry = DiaryEntry("My title", "This is five words long")
    assert diary_entry.count_words() == 5