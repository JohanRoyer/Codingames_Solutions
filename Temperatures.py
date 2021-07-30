import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

if n == 0 :
    lowest_temp = 0
else:  

    list_temp = []  #list of all listed temperatures

    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        list_temp.append(t)

    lowest_temp = list_temp[0]


    if len(list_temp) > 1 :
        for i in range (1,len(list_temp)):
            compared_temp = list_temp[i] #the temperature in the list that is being compared
            if abs(compared_temp) == abs (lowest_temp):    #if there are several lowest temperature we check if one of them is positive and pick it if it's the case
                if compared_temp == abs(compared_temp) or lowest_temp == abs (lowest_temp):
                    lowest_temp = abs(lowest_temp)
            else :   #if the temperatures are different, we pick the lowest in absolute value
                absolute_min_temp = min(abs(compared_temp),abs(lowest_temp))
                if absolute_min_temp == abs(compared_temp):
                    lowest_temp = compared_temp

            if lowest_temp == 0:   #if the lowest temperature is 0 then it can't be lower and we can stop the loop
                break
        

        





# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



print(lowest_temp)
