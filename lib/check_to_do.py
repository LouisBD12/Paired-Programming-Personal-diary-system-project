'''1. As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO
2. name of function - check_to_do
parameters - text
returns - True or False (boolean)
no side effects'''

def check_to_do(text):
    if '#TODO' in text:
        return True
    else:
        return False