import sys
import math
import numpy

# Don't let the machines win. You are humanity's last hope...

def searchNodes(direction,x,y):
    nodeFound = False
    if direction == "right":
        abscisse = x
        while abscisse <=(width-1) and not nodeFound:
            if cells_map[y][abscisse]==1:
                printNode("right",abscisse,y)
                nodeFound = True
            abscisse += 1

    if direction == "bottom":
        ordonnee = y
        while ordonnee <= (height-1) and not nodeFound:
            if cells_map[ordonnee][x]==1:
                printNode("bottom",x,ordonnee)
                nodeFound = True
            ordonnee += 1


#search the right and bottom neighbours to print the Node's coordinates, then print the coordinates of the next node in the indicated direction if there is one.
def printNode(direction,x,y):
    rightneighbour = findNeighbour("right",x,y)
    bottomneighbour = findNeighbour("bottom", x,y)

    print ("{} {} {} {} {} {}".format(x,y,rightneighbour[0],rightneighbour[1],bottomneighbour[0], bottomneighbour[1]))
    if direction == "right" and rightneighbour[0] != -1:
        printNode("right",rightneighbour[0],y)
    if direction == "bottom" and bottomneighbour[0] != -1:
        printNode("bottom",x,bottomneighbour[1])


#find the nearest neighbour in the selected direction, return [-1,-1] if there is no neighbour
def findNeighbour(direction,x,y):
    if direction == "right":
        abscisse = x+1
        while abscisse <= width-1:
            print("abscisse:={}, y={}".format(abscisse,y), file=sys.stderr, flush=True)
            if cells_map[y][abscisse] == 1:
                return [abscisse,y]
            else : abscisse +=1
        return [-1,-1]
    if direction == "bottom":
        ordonnee = y+1
        while ordonnee <= height-1:
            if cells_map[ordonnee][x] == 1:
                return [x,ordonnee]
            else : ordonnee +=1
        return [-1,-1]

        


############################## INITIALIZATION #############################################

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
cells_map = numpy.zeros([height,width], dtype=int) #matrix representig the cells map, there is a 1 if there is a cell on the grid at index i,j and 0 if there isn't
for i in range(height):
    line = input()  # width characters, each either 0 or .
    for j in range(width):
        if line[j]== "0": #there is a cell in this case
            cells_map[i][j]=1

  
#####################################################################################################


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#we search the nodes on the right then on the bottom from the top left position of the grid and then  
for i in range (min(width,height)):
    searchNodes("right",i,i)
    if i< (height-1):
        searchNodes("bottom",i,i+1)



