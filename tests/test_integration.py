from lib.diary import *
from lib.diary_entry import *

'''adding two diary entries
should see them back in the list'''

def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry("title", "Some contents")
    entry2 = DiaryEntry("title 2", "Some contents 2") 
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1, entry2]

'''
adding two entries
using count words method which
should sum up all words in the entries '''

def test_count_words_returns_sum_of_words_in_all_contents_of_entries():
    diary = Diary()
    entry1 = DiaryEntry("title", "Some contents")
    entry2 = DiaryEntry("title 2", "Some contents 2") 
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 5

'''given i add two entries with a total word count of 5
and my reading speed is 2 wpm
it should return that it will take 3 mins'''

def test_reading_time_it_takes_to_read_all_entries():
    diary = Diary()
    entry1 = DiaryEntry("title", "Some contents")
    entry2 = DiaryEntry("title 2", "Some contents 2") 
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(2) == 3

'''given i add two diary entries, one long and one short
and i call find_best_entry_for_reading_time
with a wpm and minutes that means i can only read the short one
then find_best_entry_for_reading_time returns the shorter one'''

def test_find_best_entry_for_reading_time_reutrns_entry_that_fits_in_time():
    diary = Diary()
    entry1 = DiaryEntry("title", "Some contents")
    entry2 = DiaryEntry("title 2", "Some contents 2 three four five six seven") 
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1

'''given i add a diary entry
and i call find_best_entry_for_reading_time
with a wpm nd minutes that means i can read that entry
then find_best_entry_for_reading_time returns that entry'''

def test_finds_best_entry_for_reading_time_returns_single_entry_that_fits_in_time():
    diary = Diary()
    entry1 = DiaryEntry("title", "Some contents")
    entry2 = DiaryEntry("title 2", "Some contents 2 three four five six seven") 
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry1

'''given i add a diary entry
and i call find_best_entry_for_reading_time
with a wpm nd minutes that means i cannot read that entry
then find_best_entry_for_reading_time returns None'''

def test_find_best_entry_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    diary = Diary()
    entry1 = DiaryEntry("title", "Some contents 1 2 3 4 5 6 7") 
    diary.add(entry1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

'''given i add two diary entries
and i call find_best_diary_entry_for_reading_time
with a wpm and minutes that means I could read both
then find_best_diary_entry_for_reading_time returns the longer one
'''
def test_find_best_entry_for_reading_time_returns_the_longest_readable():
    diary = Diary()
    entry1 = DiaryEntry("title", "Some contents")
    entry2 = DiaryEntry("title 2", "Some contents 2 three four five six seven") 
    diary.add(entry1)
    diary.add(entry2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry2

