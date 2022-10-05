from convert3 import *
from math import *
import keyboard
import random
import cv2
import numpy as np
import time

#Laplace equation solution
#divergence of the gradient of potential = +-density * constant

#therefore, the height value at any position (coords[i][j][2]) is the potenital energy


#setup
img = np.zeros((1080,1920,3), np.uint8)



theta=60*pi/180
obsx=0
obsy=0
obsz=-20
betax=0
speed=1
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
k=.2
t=0

length=50

#create initial conditions
for i in range(length):
    add=[]
    for j in range(length):
        #x=0,y=0,u=0
        vx,vy,vu,m=0,0,0,5
        add.append([i,j,0,vx,vy,vu,m])
    coords.append(add)

#create boundaries
for j in range(length):
    coords[j][0][2]=40*sin(j*pi/(length-1))
    coords[j][length-1][2]=0#40*sin(j*pi/(length-1))


while True:
    t+=dt

    #dynamic boundaries
    for j in range(length):
        bereal=0
        coords[j][0][2]=40*sin(t*.1+j*.1)
        coords[j][length-1][2]=40*cos(t*.1+j*.1)
        #coords[j][length-1][2]=40*sin(t*.02)
        #coords[0][j][2]=40*sin(t*.08)
        #coords[length-1][j][2]=40*sin(t*.06)
    
    
    #ends are free
    for j in range(1,length-1):
        #along i=0
        u0=coords[0][j][2]
        u1=coords[0][j-1][2]
        u2=coords[0][j+1][2]
        u3=coords[1][j][2]
        #print(u0,u1,u2,u3)
        fu=k*(u2-u0)+k*(u1-u0)+k*(u3-u0)
        m=coords[0][j][6]
        vu=coords[0][j][5]
        a=scale*fu/m
        vu+=a*dt
        u0+=vu*dt
        coords[0][j][2]=u0

        #along i=length-1; which is the other end
        u0=coords[length-1][j][2]
        u1=coords[length-1][j-1][2]
        u2=coords[length-1][j+1][2]
        u3=coords[length-2][j][2]
        fu=k*(u2-u0)+k*(u1-u0)+k*(u3-u0)
        m=coords[length-1][j][6]
        vu=coords[length-1][j][5]
        a=scale*fu/m
        vu+=a*dt
        u0+=vu*dt
        coords[length-1][j][2]=u0
        bereal=5
    
        
    
        

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

            fu=k*(u2-u0)+k*(u4-u0)+k*(u1-u0)+k*(u3-u0) #hooke's law
            a=scale*fu/m #convert to acceleration from force (scale by 10)
            vu+=a*dt #velocity changes because of acceleration
            u0+=vu*dt #position changes because of velocity
            coords[i][j][2]=u0 #set position as new updated position

    cnew=[]
    for i in range(length):
        for j in range(length):
            cnew.append([coords[i][j][1],coords[i][j][2],coords[i][j][0]])

                
    
    #convert 3d to 2d and draw circles
    a=convert(cnew,theta,obsx,obsy,obsz,betax)
    img = np.zeros((1080,1920,3), np.uint8)

    for i in range(len(a)):
        use=a[i]
        x=use[0]*1920
        y=use[1]*1080
        center=(round(x)+offx,round(y)+offy)
        #print(center)
        color=(150,250,100)

        if i<length: #convert i number to position in coords matrix
            loci=0 #location i
            locj=i #location j
        if i>=length:
            loci=floor(i/length)
            locj=i%length

        z1=coords[loci][locj][0] #determine depth into screen(match 3rd from above)
        vz=coords[loci][locj][3]#get location of vu in matrix from like i =75 to [][]
        if obsz<(z1+vz*dt):
            cv2.circle(img,center,2,color,-1)
    
    cv2.imshow("wave eq", img)
    cv2.waitKey(1)
    
    if keyboard.is_pressed('w'):
        obsz+=10*speed
    if keyboard.is_pressed('s'):
        obsz-=10*speed
    if keyboard.is_pressed('a'):
        betax+=1
    if keyboard.is_pressed('d'):
        betax-=1
    if keyboard.is_pressed('up arrow'):
        obsy+=speed*-1
    if keyboard.is_pressed('down arrow'):
        obsy-=speed*-1
    if keyboard.is_pressed('right arrow'):
        obsx+=speed
    if keyboard.is_pressed('left arrow'):
        obsx-=speed


