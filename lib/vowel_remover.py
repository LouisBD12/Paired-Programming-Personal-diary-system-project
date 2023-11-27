class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        result = ""
        for char in self.text:
            if char.lower() not in self.vowels:
                result += char
        return result