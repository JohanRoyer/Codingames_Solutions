import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while 1:
    highest_mountain = 0  #initialisation size of the highest mountain
    target_mountain = 0    #number of the mountain that will be shot
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if highest_mountain < mountain_h:
            highest_mountain = mountain_h
            target_mountain = i
    

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # The index of the mountain to fire on.

    print(target_mountain)   
