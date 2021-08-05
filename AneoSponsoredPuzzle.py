import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


################### WORKING SOLUTION - CODE NEEDS TO BE CLEANED AND COMMENTED  #############

#################### FUCNTIONS ########################################

# check if the car will reach a light when it is green at the given maximum speed, if it's not the case the speed will be reduced so the car will reach it as soon as it turns green

def speed_max_light(speed,distance,duration):

    time_reach_light = round(distance/speed,5)          # which turn the car will reach the light at max speed
                                                        #value is rounded with a precision of 5 to prevent errors due to float precision with Python

    cycle_number = time_reach_light//duration  #at wich cycle of the light the car will reach it.

    #if cycle_numer is even then the light is green, if it's odd it's red
    if (cycle_number/2) != cycle_number // 2:
        time_reach_light = ((cycle_number+1)*duration)    #if the light is red, the speed is reduced so the car reach it when it turns green
        speed = distance/time_reach_light

    
    return speed


#check if the car will reach all the lights in the list when they are green, if the car reaches a red light, it's speed is reduced so it reaches it when it turns green
#the new speed may not work the previously checked lights in the list though.
def check_all_lights(speed_max, light_list):
    speed_max = speed_max/3.6       #speed in km/h is converted in m/s
    for i in range(light_count):
        speed = speed_max_light(speed_max,light_list[i][0],light_list[i][1])
        speed_max= min (speed_max, speed)
    speed_max = int(speed_max*3.6) #speed is converted in km/h again and rounded down as the car's speed regulator only accept integers
    return speed_max


####################################### VARIABLES ###################################################

light_list=[]   #list of lights. One light is a list of two elements. [distance,duration]

speed = int(input()) #maximum speed on the road

light_count = int(input())
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    light_list.append([distance,duration])

speed_max = speed
############################## PROGRAM ################################



new_speed_max = check_all_lights(speed_max,light_list)
while new_speed_max != speed_max :                      #if the speed is changed in check_all_lights, we don't know if the new speed will work with the first lights, so we need to check again
    speed_max=new_speed_max
    new_speed_max=check_all_lights(speed_max,light_list)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
print(speed_max)
