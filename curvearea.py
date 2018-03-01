# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 14:15:05 2018

@author: John Doe
"""

#AREA UNDER A CURVE
import math as ma
import numpy as np
import numpy.random as rand
import matplotlib
import matplotlib.pyplot as plot

"""
Initialization stuff
"""

mst=4
bst=9

apa=3
bpa=-5
cpa=7.6

aex=9
bex=1.1
cex=6

deltax=float(raw_input("Please choose a value for delta x. This will determine how long the calculation takes, and how accurate it is. Delta x should be a float: "))
#inter=raw_input("Please choose an interval for this program to calculate area under. This should be formatted as '2,8', no space after the comma: ")
#commaspot=inter.find(",")
#if commaspot==-1:
#    print("You have failed to enter two values, or did not include a comma. Please try again")
#start=float(inter[0:commaspot])
#end=float(inter[commaspot+1:])
start=1
end=5


def straight_line(xs,ms,bs): #Outputs a y value for every x value
    ys=float(ms)*float(xs)+float(bs)
    return ys

def parabola(xp,ap,bp,cp):
    yp=float(ap)*float(xp)*float(xp)+float(bp)*float(xp)+float(cp)
    return yp

def exponential(xe,ae,be,ce):
    ye=(float(ae)*float(xe)+float(be))*ma.exp(-float(ce)*float(xe))
    return ye
print(parabola(0,10,5,6))

num_steps=int(ma.ceil((end-start)/deltax))
print(num_steps)

"""
Computations
"""
"""
#midpoint sum
straightcomp=0
paracomp=0
exponencomp=0
for xpos in range(num_steps):
    current_x=start+deltax*xpos
    straightcomp=straightcomp+deltax*straight_line((current_x+(deltax/2)),mst,bst)
    paracomp=paracomp+deltax*parabola((current_x+(deltax/2)),apa,bpa,cpa)
    exponencomp=exponencomp+deltax*exponential((current_x+(deltax/2)),aex,bex,cex)

print("We calculated an area under the curve of "+str(straightcomp)+ " for the straight line, an area of "+str(paracomp)+" for the parabola, and an area of "+str(exponencomp)+" for the more complicated exponential function.")









"""



"""
#Point filling for area calculation
#==================================
"""
xdotfill=[]
ydotfill=[]

dotnum=100

for n in range(dotnum):
    xdotfill.append(np.random.randint(1,10))
    ydotfill.append(np.random.randint(1,10))

print xdotfill
print ydotfill
