from math import *

def convert(info,theta,obsx,obsy,obsz,betax):
    dd=10**-200
    tot=tan(theta)
    proj=[]
    for i in range(len(info)):
        proj.append([0,0])
    for i in range(len(info)):
        #y
        use=info[i]
        #print(use)
        dz=use[2]-obsz
        #print((obsy-use[1])**2+(obsz-use[2])**2)
        ryz=((obsy-use[1])**2+(obsz-use[2])**2)**.5
        dxz=((obsx-use[0])**2+(obsz-use[2])**2)**.5
        #print(dz,ryz)
        #print(dz/ryz)
        #not dz
        dy=use[1]-obsy
        phi1=acos(dy/(ryz+dd))
        phi2=phi1+(pi/2)

        #2nd and 4th are the same in this print vvv
        #print(ryz*sin(phi1),ryz*sin(phi2),dy,dz)
        #print(abs((abs(ryz*sin(phi1))-abs(dy))/dy))
        #if abs(abs(ryz*sin(phi1))-abs(dy))<.01:
        
        #if abs((abs(ryz*sin(phi1))-abs(dy))/dy)<.01:
        phix=phi1
            #print("hello")
            
        #if abs(abs(ryz*sin(phi2))-abs(dy))<.01:
        #if abs((abs(ryz*sin(phi2))-abs(dy))/dy)<.01:
            #print(dz,ryz*cos(phi2)) #yup
        phix=phi2
            #print("hello2")
            
        #print(phix)
        #if phix-betax>=theta and phix-betax<=180-theta:
        #phix=0
        #thetax=0
        yp=(use[1]-obsy)/(2*(dxz+dd))*tot+.5#(ryz*cos(phix-betax)-obsy)/(2*dxz)*tan(theta)+.5
        #print(ryz*cos(phix-betax),use[1])
        #yp=(ryz*cos(phix-betax)-obsy)/(2*dxz)*tan(theta)+.5
        #print(yp)
        proj[i][1]=yp

        #x
        rxz=((obsx-use[0])**2+(obsz-use[2])**2)**.5
        dyz=((obsy-use[1])**2+(obsz-use[2])**2)**.5
        phi1=asin(dz/(rxz+dd))
        phi2=phi1+(pi/2)
        dy=obsy-use[1]
        dx=obsx-use[0]
        #print(rxz)
        #print(phi2)
        if rxz*cos(phi1)-dx<.000001:
            phiz=phi1
        if rxz*cos(phi2)-dx<.000001:
            phiz=phi2
        #if phiz-betaz>=theta and phiz-betaz<=180-theta:
        xp=(use[0]-obsx)/(2*dyz+dd)*tot+.5#(rxz*cos(phiz-betaz)-obsx)/(2*dyz+dd)*tan(theta)+.5
        #print(xp)
        proj[i][0]=xp
    return proj
