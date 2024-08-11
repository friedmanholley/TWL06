#class ComputerPlayer extends Player, containing a program which tries to
#identify anagrams as the user is doing so

from player import Player
from itertools import permutations
from TWL06 import twl 


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__("Computer")
        #come back to implement leveling?
    
    def take_turn(center_tiles, all_word_lists):
        found_a_word = False
        while(not found_a_word):
            found_a_word = True
        
    def find_anagram(center_tiles, all_word_lists, valid_words):
        # Iterate through each word in all_word_lists
        for word in all_word_lists:
            # Iterate through different lengths of center_tiles to combine with the word
            for i in range(1, len(center_tiles) + 1):
                # Generate all permutations of center_tiles of length i
                for combo in permutations(center_tiles, i):
                    # Form a new word by adding the permutation to the original word
                    new_word = ''.join(sorted(word + ''.join(combo)))
                    # Check if the new_word is a valid word (anagram)
                    if twl.check(new_word):
                        return new_word  # Return the first anagram found
        
        return None  # Return None if no anagram is found
