import random

class Tiles:
    def __init__(self):
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
        self.unused = []
        self.center = []
        for letter, count in letter_distribution.items():
            self.unused.extend([letter] * count)
        random.shuffle(self.unused)
    
    def shuffle_tiles(self):
        random.shuffle(self.unused)

    def draw_tile(self):
        if self.unused:
            tile = self.unused.pop()
            self.center.append(tile)
            return tile
            return self.center.pop()
        else:
            return None