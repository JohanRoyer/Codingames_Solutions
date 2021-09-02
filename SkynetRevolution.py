import sys
import math
import numpy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



#return true if a gateway is in the nodes on the path 
def isgatewayonthepath(node,gateway_list):
    for gateway in gateway_list:
        if node == gateway:
            return True
            
    return False

def cutlink(explored_node, node, adjacency_matrix):
    print("test2 = {} , {}".format(explored_node, node), file=sys.stderr, flush=True)
    adjacency_matrix[explored_node][node]=adjacency_matrix[node][explored_node] = 0
    


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways


n, l, e = [int(i) for i in input().split()]

A = numpy.zeros([n,n], dtype = int) #A is the adjacency matrix for the graph

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    A[n1][n2]= 1
    A[n2][n1]=1 

gateway_list = [] # list the index of the gateway nodes

for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateway_list.append(ei)


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    
    #We start Breadth First Search algorithm to find the nearest gateway to the agent and cut the link connecting to it
    #we copy the adjacency matrix A and remove the explored nodes from the copy so we don't go several time in the same node
    explored_nodes = [si]
    explored_A = A.copy()
    for i in range (n):
            explored_A[i][si]=0
    

    explore = True

    #the nth loop will give the nodes accessible in n turns by the agent. The loop stop when a gateway is accessible
    while explore:
       
        next_nodes = []
        
        #we make the list of the next nodes accessed from the list of explorednodes
        #as soon as a node is added to explored_nodes, it is removed from the temporary adjacency matrix
        for explored_node in explored_nodes:
            for node in range (n):
                if explored_A[explored_node][node]==1 :
                    # if there is a link we check if the node is a gateway and if we didn't already cut a link this turn  before cutting the link.
                    if isgatewayonthepath(node,gateway_list):

                        #we cut the link only if explore is true to prevent cutting the link of several gateways if they are at the same distance from the agent.
                        if explore :
                            cutlink(explored_node,node, A)
                            link = [explored_node,node] #the cut link for this turn

                        explore = False
                        
                        
                        

                    next_nodes.append(node)
                    for i in range (n):
                        explored_A[i][node]=0 #once a node is reached it can't be reached again but we can still explore from it's position
        explored_nodes = next_nodes            

    print("{} {}".format(link[0],link[1]))
                


                    
                
            

    #while pas de gateway, check les noeuds liés suivants partant de si, regarde si c'est des gateway
    #si un, le coupe. Si plusieurs coupe le premier
    #peut optimiser mais première solution

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
