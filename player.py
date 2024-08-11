from TWL06 import twl

class Player:
    def __init__(self,name):
        self.name = name
        self.word_list = []
        self.score = 0
        
    #calculates the points a word is worth: word length - 3
    def word_score(word):
        return(len(word)-3)
        
    def add_word(self, word):
        self.word_list.append(word)
        self.score += self.word_score(word)
        
    def remove_word(self, word):
        self.word_list.remove(word)
        self.score -= self.word_score(word)
        
    def get_word_list(self):
        return self.word_list
            
    # Check if a word is valid
    def is_valid_word(word, center_tiles):
        temp_center = center_tiles.copy()
        for c in word:
            if c in temp_center:
                temp_center.remove(c)
            else:
                print(f"\nThere are not enough copies of '{c}' to form '{word}.'")
                return False
        if len(word) >= 4:
            if twl.check(word.lower()):
                return True
            else:
                print(f"\nThe word '{word}' is not in our dictionary. Sorry!")
        else:
            print(f"\nThe word '{word}' is too short. It must be at least 4 characters long.")
            return False
        
    def take_turn(self, center_tiles, all_words):
        word = input("\nEnter a word you want to form, or press enter to draw a new tile: ").strip().upper()
        while not word == '':
            if self.is_valid_word(word, center_tiles):
                self.add_word(word)
                for c in word:
                    center_tiles.remove(c)
                print(f"\n{word} added to player's word list: {self.get_word_list()}")
            else:
                print("Try again.")
            word = input(f"\nThe center tiles are: {center_tiles}\nEnter a word you want to form,"
                         " or press enter to draw a new tile: ").strip().upper()
