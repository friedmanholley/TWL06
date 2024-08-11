
from player import Player
from computer_player import ComputerPlayer
from tiles import Tiles

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

