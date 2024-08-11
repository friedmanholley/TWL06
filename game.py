import threading
import time
from player import Player
from computer_player import ComputerPlayer
from tiles import Tiles


def turn():
    new_tile = tiles.draw_tile()
    if new_tile:
        print(f"\nNew tile '{new_tile}' added to center tiles: {center_tiles}")
    else:
        print("No more tiles to draw.")
    for p in players:
        print(f"\n{p.name}'s word list: {p.word_list}")
        
def instructions():
    print(
        "\nAnagrams is a tile-based word game that involves rearranging "
          "letter tiles to form words.\nThe game pieces are a set of tiles "
          "with letters on one side.\nTiles are shuffled face-down then "
          "turned over one by one. \nPlayers form words by combining "
          "the letters with existing words, their own or others. \n"
          "Players can also form words entirely from center tiles.\n"
          "Here are some other rules to keep in mind: \n"
          "   1. All words must be at least 4 letters. \n"
          "   2. No proper nouns, hyphenated words, contractions, etc. "
          "Words are checked in the TWL06 Scrabble Dictionary.\n"
          "   3. Your score is equal to the total number of tiles in your word list, "
          "minus the number of words times three.\n"
          #add rule about changing root meaning if able to implement
    )
    
# Start the game by drawing the initial 3 tiles
def start_game():
    user_input = input(
        f"\nWelcome {player.name}! Press 'I' and then enter "
        "to view game instructions, or just press Enter to start "
        "the game: "
    )
    if user_input.upper()=='I':
        instructions()
    for _ in range(3):
        tiles.draw_tile()

if __name__ == "__main__":
    player = Player(name=input("What's your name? "))

    
    computer = ComputerPlayer()
    players = [player, computer]
    tiles = Tiles()
    unused_tiles = tiles.unused
    center_tiles = tiles.center
    start_game()
    #while(unused_tiles):
    turn()

