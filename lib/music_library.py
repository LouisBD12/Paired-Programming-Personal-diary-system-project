'''As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.'''

class Music():
    def __init__(self):
        self.music_library = []
    
    def music_add(self, song):
        self.music_library.append(song)
        return self.music_library