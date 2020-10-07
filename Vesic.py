import math
from Meyerhof import *
from Terzaghi import *


def Vesic(h,gamma,c,fi,B,L,Df,fs):
    g=9.81                  #kN/m^2

    if L/B>=2:
        if fi>34:
            fi=1.5*fi-17    #degree
        else:
            fi=fi           #degree
    else:
        fi=fi               #degree
    
    if Df/h<1:
        sigmazD=gamma*Df     
    else:
        sigmazD=gamma*h+(gamma-g)*(Df-h)
    
    if h-Df>=B:
        gamma=gamma
    elif h-Df<=0:
        gamma=gamma-g
    elif h-Df<B:
        gamma=gamma-g+((h-Df)/B)*g

    fiR=fi*math.pi/180      #radian
    
    a=math.exp(math.pi*(math.tan(fiR)))

    Kp=math.tan((math.pi/4)+(fiR/2))**2

    #------------BEARING CAPACITY FACTORS-------------#
    #-------------------------------------------------#

    Nq=a*Kp
    if fi==0:
        Nc=5.14
    else:
        Nc=(Nq-1)*(1/math.tan(fiR))
    Ngamma=2*(Nq+1)*math.tan(fiR)

    #-------------------SHAPE FACTORS-----------------#
    #-------------------------------------------------#

    sc=1+(Nq/Nc)*(B/L)
    sq=1+(B/L)*math.tan(fiR)
    if 1-0.4*B/L>=0.6:
        sgamma=1-0.4*B/L
    else:
        sgamma=0.6

    #-------------------DEPTH FACTORS-----------------#
    #-------------------------------------------------#
    if Df/B<=1:
        dc=1+0.4*Df/B
        dq=1+2*math.tan(fiR)*((1-math.sin(fiR))**2)*(Df/B)
    else:
        dc=1+0.4*math.atan(Df/B)
        dq=1+2*math.tan(fiR)*((1-math.sin(fiR))**2)*math.atan(Df/B)
    
    dgamma=1

    #------------BEARING CAPACITY FACTORS-------------#
    #-------------------------------------------------#

    qult=c*Nc*sc*dc + sigmazD*Nq*dq*sq + 0.5*gamma*B*Ngamma*sgamma*dgamma               #kPa
    qall=qult/fs                #kPa

    print(qult,qall,Nc,Nq,Ngamma)

Vesic(3,19,0,33,40,120,1.5,3)
Meyerhof(3,19,0,33,40,120,1.5,3)
Terzaghi("Strip Footing",3,19,0,33,40,1.5,3)



