import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    
    def __init__(self, path):
        """Read words from a file and initialize the word list."""
        self.word_list = self.read_words_from_file(path)
        print(f"{len(self.word_list)} words read")
        
    def read_words_from_file(self, path):
        """Read words from the given file and return a list of words."""
        with open(path, 'r') as file:
            words = [line.strip() for line in file]
        return words
        
    def random(self):
        """Return a random word from the word list."""
        return random.choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, excluding comments and blank lines."""
    
    def read_words_from_file(self, path):
        """Read words from the given file, excluding comments and blank lines."""
        with open(path, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        return words

# Using WordFinder with word.txt
wf = WordFinder("word.txt")
print(wf.random())
print(wf.random())

# Using SpecialWordFinder with word.txt
swf = SpecialWordFinder("word.txt")
print(swf.random())
print(swf.random())
