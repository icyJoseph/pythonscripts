import numpy as np
import random
import matplotlib.pyplot as plt

#funcion to tumble
def spill(spilledPile, d):
    tumbles = 0
    flag = True
    while flag is True:
        for i in range (0, d):
            for j in range (0, d):
                if spilledPile[i][j] > 3:
                    spilledPile[i][j]  = spilledPile[i][j] - 4
                    tumbles = tumbles + 1
                    if i  > 0 :
                        spilledPile[i-1][j] = spilledPile[i-1][j] + 1
                    if i  < d - 1 :
                        spilledPile[i+1][j] = spilledPile[i+1][j] + 1
                    if j  > 0 :
                        spilledPile[i][j-1] = spilledPile[i][j-1] + 1
                    if j  < d - 1 :
                        spilledPile[i][j+1] = spilledPile[i][j+1] + 1
                    print "Partial result "+ str(tumbles) +":"+ pilePrint(spilledPile, d)
        flag = checker(spilledPile, d)
    print "Done in: "+ str(tumbles) + " steps"
    return spilledPile

#Function to check each box value is less than 3
def checker(pile, d):
    flag = False;
    for i in range (0, d):
        for j in range (0, d):
            if pile[i][j] > 3:
                flag = True;
    return flag

#Function that adds the piles
def addPile(pile1, pile2, d):
    addedPile = [[0 for x in range(d)] for y in range(d)]
    for i in range (0, d):
        for j in range(0, d):
            addedPile[i][j] = pile1[i][j] + pile2[i][j]
    return addedPile

#Function that prints the pile in 3 rows
def pilePrint(pile, d):
    matrix = "\n"
    for i in range (0, d):
        matrix = matrix + str(pile[i]) + "\n"
    return str(matrix)

#Defining the dimensions of the Matrix
d = 10
#Creating the two matrix
pileA = [[0 for x in range(d)] for y in range(d)]
pileB = [[0 for x in range(d)] for y in range(d)]

#Filling with random values between 0 and 3
for i in range (0,d):
    for j in range (0,d):
        pileA [i][j] = random.randint(0,d)
print "Pile A: " + pilePrint(pileA, d)

for i in range (0,d):
    for j in range (0,d):
        pileB [i][j] = random.randint(0,d)
print "Pile B: " + pilePrint(pileB, d)

addedPiles = addPile(pileA, pileB, d)
print "Added Piles: " + pilePrint(addedPiles, d)

#Generating the Sandpile spill/tumble
spilledPile = spill(addedPiles, d)
print "Here is the result: "+ pilePrint(spilledPile,d)
