class Player:
    def __init__(self,name):
        self.name = name
        self.word_list = []
        
    def add_word(self, word):
        self.word_list.append(word)
        
    def get_word_list(self):
        return self.word_list

