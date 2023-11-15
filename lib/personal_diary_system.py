'''A function called make_snippet that takes a string as an argument and returns the 
first five words and then a '...' if there are more than that.'''
def make_snippet(string):
    words = string.split()
    make_snippet = ' '.join(words)
    if len(words) > 5:
        make_snippet = ' '.join(words[:5]) + '...'
    return make_snippet

'''A function called count_words that 
takes a string as an argument and returns the number of words in that string.'''
def count_words(string):
    words = string.split()
    return len(words)

