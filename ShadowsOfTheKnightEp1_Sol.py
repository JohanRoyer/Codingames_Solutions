import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


########################### WORKING SOLUTION  ---   STILL NEED TO CLEEN CODE WITH FUNCTION TO PREVENT CODE DUPLICATE  #####################

################################# FUNCTIONS #######################################

#makes batman jump, changing the jumping coordonates and the extremum of the bomb's possible location depending of the axis (X or Y) and the direction (U, D, R, L)
def jumpaxis(axis, direction,coordinates_list):
    if axis == "Y":
        if direction == "U":
            jump(5,4,6,7,coordinates_list)
        else:
            jump(5,4,7,6,coordinates_list)
    else :
        if direction == "R":
            jump(1,0,3,2,coordinates_list)
        else :
            jump(1,0,2,3,coordinates_list)


def jump(jumpcoor,currentcoor,constantextremum, changedextremum, coordinates):

    coordinates[jumpcoor] = (coordinates[constantextremum]+coordinates[currentcoor])//2 #dichotomy : Jump to the midle of the current location and the extremum location in the direction of the bomb
    coordinates[changedextremum] = coordinates[currentcoor]                              #the bomb can't be in the opposite direction so the extremum concerned becomes the location before the jump





#################################### VARIABLES ####################################

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
x=x0
y=y0
minx = 0 # the bomb is located between minx and maxx and miny and maxy, the range is reduced after each jump from batman after getting info from the detector
miny = 0
maxx = w
maxy = h
x_saut=x
y_saut=y
coordinates_list = [x,x_saut,minx,maxx, y, y_saut, miny, maxy]

################################ PROGRAM ###################################################

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    if len(bomb_dir) == 1 : #one of the coordinates is correct, we don't know if it's u/d or r/l
        if bomb_dir == "U" or "D":  #case up or down, change y
            jumpaxis("Y",bomb_dir,coordinates_list)
        else:      #case right or left, change x
            jumpaxis("X",bomb_dir,coordinates_list) 

    else : # both coordinates need to be changed, the first letter is always U/D
         #change y then x
        jumpaxis("Y",bomb_dir[0],coordinates_list)
        jumpaxis("X",bomb_dir[1],coordinates_list)
                     
    coordinates_list[0] = coordinates_list[1] # current location for next turn become the jumping location of this turn
    coordinates_list[4] = coordinates_list[5]   
    



    # the location of the next window Batman should jump to.
    print("{} {}".format(coordinates_list[1],coordinates_list[5]))  # print the jumping coordinates