from lib.grammar_stats import *

def test_check():
    grammar_stats = GrammarStats()
    assert grammar_stats.check("Hello my name is Louis.") == True
    assert grammar_stats.check("hello my name is Louis.") == False
    assert grammar_stats.check("Hello my name is Louis") == False
    assert grammar_stats.check("Hello my name is Louis!") == True
    assert grammar_stats.check("Hello my name is Louis?") == True

def test_percentage_good():
    grammar_stats = GrammarStats()
    assert grammar_stats.percentage_good() == 0
    grammar_stats.check("This is a valid sentence.")
    grammar_stats.check("This is a valid sentence.")
    grammar_stats.check("This is an invalid sentence")
    assert grammar_stats.percentage_good() == 66
    grammar_stats.check("This is a valid sentence.")
    assert grammar_stats.percentage_good() == 75







