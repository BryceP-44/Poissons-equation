from convert3 import *
from math import *
import keyboard
import random
import cv2
import numpy as np
import time

#Laplace equation



img = np.zeros((1080,1920,3), np.uint8)



theta=140*pi/180
obsx=0
obsy=0
obsz=-20
betax=0
speed=2
coords=[]
dd=10**-200
dt=1
gc=5
scale=10
size=50
offx=0
offy=0
b=[]
vx=[]
vy=[]
vz=[]
m=[]
add=[]
k=.1

length=50

#create initial conditions
for i in range(length):
    add=[]
    for j in range(length):
        #x=0,y=0,u=0
        vx,vy,vu,m=0,0,0,5
        add.append([i,j,0,vx,vy,vu,m])
    coords.append(add)


scale=1000
off=100

#create boundaries
for j in range(length):
    coords[0][j][2]=0 #static
    coords[length-1][j][2]=40*sin(j*pi/(length-1)) #useless code


while True:
    #
    #put a conservative field here (make electrons(E field) or planets(g field))
    #
    
    for i in range(1,length-1):
        for j in range(1,length-1):
            #inside the pillow
            u0=coords[i][j][2]
            u1=coords[i-1][j][2]
            u2=coords[i][j+1][2]
            u3=coords[i+1][j][2]
            u4=coords[i][j-1][2]
            vu=coords[i][j][5]
            m=coords[i][j][6]

            fu=k*(u2-u0)+k*(u4-u0)+k*(u1-u0)+k*(u3-u0)
            a=10*fu/m
            #print(fu)
            #print(obj1)
            vu+=a*dt
            #print(vu)
            u0+=vu*dt
            coords[i][j][2]=u0

    this=coords[5][5]
    this=this[2]
    #print(this)

    
    #print(coords)
    #print(" ")


    cnew=[]
    for i in range(length):
        for j in range(length):
            cnew.append([coords[i][j][1],coords[i][j][2],coords[i][j][0]])

                
    #print(cnew)
    
    #convert 3d to 2d and draw circles
    a=convert(cnew,theta,obsx,obsy,obsz,betax)
    #print(a)
    img = np.zeros((1080,1920,3), np.uint8)

    for i in range(len(a)):
        use=a[i]
        x=use[0]*1920
        y=use[1]*1080
        center=(round(x)+offx,round(y)+offy)
        color=(150,250,100)

        if i<length: #convert i number to position in coords matrix
            loci=0 #location i
            locj=i #location j
        if i>=length:
            loci=floor(i/length)
            locj=i%length

        z1=coords[loci][locj][2] #get location of u
        vz=coords[loci][locj][5]#get location of vu from like i =75 to [][]
        if obsz<(z1+vz*dt):
            cv2.circle(img,center,2,color,-1)
    
    cv2.imshow("wave eq", img)
    cv2.waitKey(1)
    
    if keyboard.is_pressed('w'):
        obsz+=5*speed
    if keyboard.is_pressed('s'):
        obsz-=5*speed
    if keyboard.is_pressed('a'):
        betax+=1
    if keyboard.is_pressed('d'):
        betax-=1
    if keyboard.is_pressed('up arrow'):
        obsy+=speed
    if keyboard.is_pressed('down arrow'):
        obsy-=speed
    if keyboard.is_pressed('right arrow'):
        obsx+=speed*-1
    if keyboard.is_pressed('left arrow'):
        obsx-=speed*-1
    
    #print(ax[5],ay[5])
    #print(a)
    #print(scale*round(x)+offx,scale*round(y)+offy)


