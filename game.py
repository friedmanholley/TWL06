
from TWL06 import twl
from player import Player
from computer_player import ComputerPlayer
from tiles import Tiles


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

def turn():
    new_tile = tiles.draw_tile()
    if new_tile:
        center_tiles.append(new_tile)
        print(f"\nNew tile '{new_tile}' added to center tiles: {center_tiles}")
    else:
        print("No more tiles to draw.")
    
# Start the game by drawing the initial 3 tiles
def start_game():
    for _ in range(3):
        center_tiles.append(tiles.draw_tile())

if __name__ == "__main__":
    player = Player(name=input("What's your name? "))
    computer = ComputerPlayer()
    tiles = Tiles()
    unused_tiles = tiles.unused
    center_tiles = tiles.center
    start_game()
    while(unused_tiles):
        turn()

