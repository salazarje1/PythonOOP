"""Word Finder: finds random words from a dictionary."""
from random import choice
from readline import get_line_buffer

class WordFinder:
    """
    
    """

    def __init__(self, path):
        self.path = path
        self.lst = self.get_list()
        print(f"{len(self.lst)} word read")

    def get_list(self):
        file = open(self.path, 'r')
        new_list = [word.replace("\n", '') for word in file]
        file.close()
        return new_list

    def random(self):
        return choice(self.lst)
    

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
        self.lst = self.get_list()

    def get_list(self):
        word_list = []
        with open(self.path, 'r') as file:
            for line in file: 
                line = line.replace("\n", '')
                if not line.startswith('#'):
                    if line: 
                        word_list.append(line)
        return word_list



special_finder = SpecialWordFinder("text.txt")
print(special_finder.lst)

print(special_finder.random())
print(special_finder.random())
print(special_finder.random())

# word_finder = WordFinder('words.txt')

# print(word_finder.random())
# print(word_finder.random())
# print(word_finder.random())
# print(word_finder.random())

