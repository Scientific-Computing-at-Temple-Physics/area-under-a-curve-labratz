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

deltax=.1
#deltax=float(raw_input("Please choose a value for delta x. This will determine how long the calculation takes, and how accurate it is. Delta x should be a float: "))
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

num_steps=int(ma.ceil((end-start)/deltax))


"""
Computations
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

#Integral based computation
def integrate_straight(xs,ms,bs):
    ys=(float(ms)/2)*float(xs)**2+float(bs)*float(xs)
    return ys

def integrate_para(xp,ap,bp,cp):
    yp=(float(ap)/3)*float(xp)**3+(float(bp)/2)*float(xp)**2+float(cp)*float(xp)
    return yp

def integrate_exp(xe,ae,be,ce):
    dv=ma.exp(-float(ce)*float(xe)) #bunch of unnecessary variables in here, simply for checking
    v=-(1/float(ce))*ma.exp(-float(ce)*float(xe))
    u=(float(ae)*float(xe)+float(be))
    du=float(ae)
    vdu=-ma.exp(-float(ce)*float(xe))
    intvdu=(1/float(ce))*ma.exp(-float(ce)*float(xe))
    ye=(u*v)-intvdu
    return ye

theory_str=integrate_straight(end,mst,bst)-integrate_straight(start,mst,bst)
theory_para=integrate_para(end,apa,bpa,cpa)-integrate_para(start,apa,bpa,cpa)
theory_exp=integrate_exp(end,aex,bex,cex)-integrate_exp(start,aex,bex,cex)

print("Theoretically, the area under the straight line should be "+str(theory_str)+", the area under the parabola should be "+str(theory_para)+", and the area under the more complicated exponential curve should be " +str(theory_exp))


"""
#Point filling for area calculation
#==================================
"""

np.random.seed(3)

dotnum=10000

#DEFINING LISTS
xdotfill=[]

ysdotfill=[]
ypdotfill=[]
yedotfill=[]

ysheight_list=[]
ypheight_list=[]
yeheight_list=[]

ysdifference=[]
ypdifference=[]
yedifference=[]

#GENERATING X POINTS AND FINDING Y OF GENERATED X
for dotspot1 in range(dotnum):
    xdot=np.random.rand()+np.random.randint(start,end)
    xdotfill.append(xdot)
    
    ysheight=straight_line(xdot,2,3)
    ypheight=parabola(xdot,2,3,4)
    yeheight=exponential(xdot,2,3,4)
    
    ysheight_list.append(ysheight)
    ypheight_list.append(ypheight)
    yeheight_list.append(yeheight)

#FINDING MAX AND MINS OF FUNCTIONS
maxys=max(ysheight_list)
minys=min(ysheight_list)

maxyp=max(ypheight_list)
minyp=min(ypheight_list)

maxye=max(yeheight_list)
minye=min(yeheight_list)
    
#CREATING LIST OF RANDOM HEIGHTS IN RELATIVE GRAPH RANGE
for dotspot2 in range(dotnum):
    ysdotfill.append(np.random.rand()+np.random.randint(minys-minys*abs(2*np.std(minys)),maxys+maxys*abs(2*np.std(maxys))+1))
    ypdotfill.append(np.random.rand()+np.random.randint(minyp-minyp*abs(2*np.std(minyp)),maxyp+maxyp*abs(2*np.std(maxyp))+1))
    yedotfill.append(np.random.rand()+np.random.randint(minye-minye*abs(2*np.std(minye)),maxye+maxyp*abs(2*np.std(maxye))+1))

#CALCULATING NUMBER OF POINTS BELOW CURVE
belowpoints=0
belowpointp=0
belowpointe=0

for dotspots in range(dotnum):
    if abs(ysheight_list[dotspots])-abs(ysdotfill[dotspots])>=0:
        belowpoints=belowpoints+1
for dotspotp in range(dotnum):
    if abs(ypheight_list[dotspotp])-abs(ypdotfill[dotspotp])>=0:
        belowpointp=belowpointp+1
for dotspote in range(dotnum):
    if abs(yeheight_list[dotspote])-abs(yedotfill[dotspote])>=0:
        belowpointe=belowpointe+1

#RATIO OF POINTS BELOW CURVE
ratios=float(belowpoints)/float(dotnum)
ratiop=float(belowpointp)/float(dotnum)
ratioe=float(belowpointe)/float(dotnum)

print ratios, ratiop, ratioe

#AREA OF SURVEYED GRAPH
totareas=-(minys-minys*abs(2*np.std(minys))-(maxys+maxys*abs(2*np.std(maxys))+1))
totareap=-(minyp-minyp*abs(2*np.std(minyp))-(maxyp+maxyp*abs(2*np.std(maxyp))+1))
totareae=-(minye-minye*abs(2*np.std(minye))-(maxye+maxyp*abs(2*np.std(maxye))+1))

#CALCULATING AREA OF CURVES
dotareas=ratios*totareas
dotareap=ratiop*totareap
dotareae=ratioe*totareae

print dotareas, dotareap, dotareae
