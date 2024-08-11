class Player:
    def __init__(self,name):
        self.name = name
        self.word_list = []
        
    def add_word(self, word):
        self.word_list.append(word)
        
    def get_word_list(self):
        return self.word_list

    def take_turn():
        word = input("\nEnter a word you want to form, or press enter to draw a new tile: ").strip().upper()
        while not word == '':
            if is_valid_word(word):
                player.add_word(word)
                for c in word:
                    center_tiles.remove(c)
                print(f"\n{word} added to player's word list: {player.get_word_list()}")
            else:
                print("Try again.")
            word = input(f"\nThe center tiles are: {center_tiles}\nEnter a word you want to form, or press enter to draw a new tile: ").strip().upper()
