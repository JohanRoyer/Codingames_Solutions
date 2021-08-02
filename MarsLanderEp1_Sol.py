import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]


############# A solution which optimizes fuel consomption. ###############################
# Note : We can still reduce fuel consomption in the case where the lander lands between the time it needs to reduce it's acceleration and the time it reaches max power
#But the fuel consomption would be reduced by 5-6 max, which could be considered negligible here.

mars_gravity = 3.771
crash_speed = -40
max_power = 4

def power_up (power): #can only increment the power by 1 per turn
    if power < max_power:
        power += 1
    return power

def power_down (power):
    if power > 0:
        power -= 1
    return power

def speed_check(speed, power): #check if mars lander will be able to decrease it's speed before it reaches 40 m/s at it's current power knowing it can increment it's power by 1 per turn max
    speed_max = speed  #maximum speed reached if we start increasing power now
    for i in range(power,max_power + 1):
        speed_max -= mars_gravity - i
    is_safe =   speed_max > crash_speed


    return is_safe   # if it returns false, we need to increase power the next turn or we risk a crash



# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if power == max_power and crash_speed < v_speed -mars_gravity + (max_power - 1) : #if the lander is at max speed, check if the speed was reduced enough to allow powering down while being safe
        power = power_down(power)

    elif not speed_check(v_speed, power):           #increase power if the landing speed is too high for safety
        power = power_up(power)


    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print("0 {}".format(power))
