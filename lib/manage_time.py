'''As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.'''
def reading_time(words):
    mins = words / 200
    if str(mins)[-1] == '0' and str(mins)[-2] == '.':
        mins = int(mins)
    return f"{mins} minutes"
