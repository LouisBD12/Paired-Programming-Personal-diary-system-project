from lib.music_library import *

def test_music_add():
    music = Music()
    assert music.music_add("Jingle Bells") == ["Jingle Bells"]
    assert music.music_add("Silent Night") == ["Jingle Bells", "Silent Night"]