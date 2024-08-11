# COMS W3132 Individual Project
## Author
Gabrielle Friedman
gf2501@columbia.edu

## Project Title 
Anagrams

## Project Description
Anagrams is a multi-player word game played using the following letter distributions
from the tile game bananagrams:
    2: J, K, Q, X, Z
    3: B, C, F, H, M, P, V, W, Y
    4: G
    5: L
    6: D, S, U
    8: N
    9: T, R
    11: O
    12: I
    13: A
    18: E

The game begins with 3 tiles facing up and the rest facing down. On each turn, 
a tile is flipped. Players may then:
1) form a word entirely from the center tiles
2) 'steal' a word from another player's list by anagramming the word (and 
    changing the root meaning)
3) 'defend' a word from their own list by anagramming the word (and changing 
    the root meaning)

Words must be 4+ letters long. Each word is worth its length minus three points. 
When the facedown tiles are gone, and either the center tiles are gone or all 
players agree there are no further moves to be made, the game ends. 
Highest score wins.

I really enjoy playing this game with my family. It's definitely something that
takes practice, and now that I no longer live at home, I'm always rusty when
I do get home to play. And then I lose. This version, where I can play against
a computer, will help me keep my skills sharp. And entertain me.

## Requirements, Features and User Stories
A computer player which is capable of simulating human play by simultaneously 
attempting to create words from the center tiles and attempting to anagrams words
in the various word lists.

A text-based interface for the player to submit words and a process for 
determining whether those words are valid moves.

Down the road, I hope to create a visual representation of this game which can 
be played as an app.

##Technical Specifications
I am using the submodule TWL06, which I found on github, from Michael Fogleman. 
See the link to the public repository:
https://github.com/fogleman/TWL06/tree/7e1ca3f9924018027408573ccdc7f22900f144d4

I'm also implementing threading in order to allow the computer and human user
to simultaneously attempt the task of finding an anagram.

## System or Software Architecture Diagram
*Include a block-based diagram illustrating the architecture of your software or
system. This should include major components, such as user interface elements,
back-end services, and data storage, and show how they interact. Tools like
Lucidchart, Draw.io, or even hand-drawn diagrams photographed and uploaded are
acceptable. The purpose of the diagram is to help us understand the architecture of
your solution. Diagram asthetics do not matter and will not be graded.*

## Development Methodology
I will start by writing classes for game and player.
I will then extend player to computer_player.
I determined I needed a tiles class, and developed.
Next is integration of TWL06 submodule as dictionary.
First I will write a functional single player version using only center tiles.
I will test manually.
Then I will work on multiplayer.
I will then tackle stealing/defending words and how the word checker can
determine which word is being anagrammed.

I will recruit my family members who also like to play this game as testers.

## Potential Challenges and Roadblocks
When I first started this, I wasn't sure how to check words. Finding and 
reading the documentation of the TWL06 library helped a lot! 

Migrating from text-based to visual is something I don't know if I have the 
coding skill to accomplish. 

## Additional Resources
https://en.wikipedia.org/wiki/Anagrams_(game)

## Conclusion and Future Work
*Wrap up your project description with any final thoughts, expectations, or goals
not covered in the sections above. Also briefly discuss potential future work,
i.e., what could be done next to improve the project.*
