from lib.tasks import *

def test_add():
    tasks = Tasks()
    assert tasks.add("Hello") == ["Hello"]
    assert tasks.add("Goodbye") == ["Hello", "Goodbye"]
    assert tasks.add("Bonjour") == ["Hello", "Goodbye", "Bonjour"]

def test_completed_tasks():
    tasks = Tasks()
    tasks.add("Hello") == ["Hello"]
    tasks.add("Goodbye") == ["Hello", "Goodbye"]
    tasks.add("Bonjour") == ["Hello", "Goodbye", "Bonjour"]
    assert tasks.completed_task("Goodbye") == ["Hello", "Bonjour"]
    assert tasks.completed_task("Bonjour") == ["Hello"]
    assert tasks.completed_task("Hello") == []
    
