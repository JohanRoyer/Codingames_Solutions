import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

horizontal_dist = light_x - initial_tx #how many cases on the right (or on the left if >0) Thor must go to catch the hammer
vertical_dist = light_y - initial_ty  #how many cases on the bottom (or on the top if >0) Thor must go to catch the hammer

def direction (distance, direction, oppositeDirection):    #depending of the relative position of THor and the hammer on an axis, says in which direction it must go ("S" and "N" or "E" and "W")
    if distance >0:
        return direction
    if distance <0:
        return oppositeDirection
    else:
        return ""



def move (distance):
    if distance >0:
        distance -=1
        return distance
    if distance <0:
        distance +=1
        return distance
    else:
        return 0




# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    horizontal_direction = direction(horizontal_dist, "E", "W")
    vertical_direction = direction(vertical_dist,"S", "N")

    horizontal_dist = move(horizontal_dist)
    vertical_dist = move(vertical_dist)
    

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    move_dir = "{}{}".format(vertical_direction,horizontal_direction)
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move_dir)
