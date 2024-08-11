#class ComputerPlayer extends Player, containing a program which tries to
#identify anagrams as the user is doing so

from player import Player 
from TWL06 import twl

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer")
        #come back to implement leveling?
    
    def find_anagrams(center_tiles, all_words):
        # Combine center_tiles into a single string, if it's a list
        if isinstance(center_tiles, list):
            center_tiles = ''.join(center_tiles)
        
        for w in all_words:
            # Check if a valid anagram can be formed
            found_word = twl.anagram(w + center_tiles)
            if found_word:
                return found_word  # Return the first valid word found
        
        return None  # Return None if no valid word is found

