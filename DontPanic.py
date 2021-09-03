import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



def order(clone_floor,clone_pos,elevator_list,exit_floor,exit_pos,direction):
    if clone_floor == -1:

        return("WAIT")
    else:
        if clone_floor>0:
            if clone_pos == elevator_list[clone_floor-1]:#We need to be carefull not to block the elevator below
                return("WAIT")
        


    
            
    
        if clone_floor == exit_floor:
            instruction = goOrBlock(clone_pos,exit_pos,direction)
            return instruction
        else:
            instruction = goOrBlock(clone_pos,elevator_list[clone_floor],direction)
            return instruction
            


#return WAIT or BLOCK if the clone goes in the direction of his target or not
def goOrBlock(clone_pos, target_pos, direction):
    if clone_pos < target_pos:
        if direction == "LEFT":
            return("BLOCK")
        else :
            return ("WAIT")
    if clone_pos > target_pos:
        if direction == "RIGHT":
            return("BLOCK")
        else:
            return("WAIT")
    else :
        return("WAIT")

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator_list = {}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevator_list[elevator_floor] = elevator_pos #there is only one elevator per floor so this works

# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    result = order(clone_floor,clone_pos,elevator_list,exit_floor,exit_pos,direction)
    print(result)
    



