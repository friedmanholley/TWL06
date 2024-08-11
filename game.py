import random
from TWL06 import twl
from player import Player

# Define the letter distribution
letter_distribution = {
    'J': 2, 'K': 2, 'Q': 2, 'X': 2, 'Z': 2,
    'B': 3, 'C': 3, 'F': 3, 'H': 3, 'M': 3, 
    'P': 3, 'V': 3, 'W': 3, 'Y': 3,
    'G': 4, 'L': 5, 
    'D': 6, 'S': 6, 'U': 6, 
    'N': 8, 
    'T': 9, 'R': 9, 
    'O': 11, 
    'I': 12, 
    'A': 13, 
    'E': 18
}

# Create a list of tiles based on the distribution
tiles = []
center_tiles = []

for letter, count in letter_distribution.items():
    tiles.extend([letter] * count)

# Shuffle the tiles randomly
random.shuffle(tiles)

# Function to draw a tile
def draw_tile():
    if tiles:
        return tiles.pop()
    else:
        return None

# Check if a word is valid
def is_valid_word(word):
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

# Function to take a turn
def take_turn(player):
    new_tile = draw_tile()
    if new_tile:
        center_tiles.append(new_tile)
        print(f"\nNew tile '{new_tile}' added to center tiles: {center_tiles}")
    else:
        print("No more tiles to draw.")
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

# Start the game by drawing the initial 3 tiles
def start_game():
    for _ in range(3):
        center_tiles.append(draw_tile())

if __name__ == "__main__":
    player = Player(name=input("What's your name? "))
    start_game()
    while(tiles):
        take_turn(player)

