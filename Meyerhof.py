import math

def Meyerhof(h,gamma,c,fi,B,L,Df,fs):
    
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

    #-------------------SHAPE FACTORS-----------------#
    #-------------------------------------------------#

    sc=1+0.2*Kp*B/L
    sq=1+0.1*Kp*B/L
    sgamma=1+0.1*Kp*B/L

    #-------------------DEPTH FACTORS-----------------#
    #-------------------------------------------------#

    dc=1+0.2*Kp**0.5*Df/B
    dq=1+0.1*Kp**0.5*Df/B
    dgamma=1+0.1*Kp**0.5*Df/B

    #------------BEARING CAPACITY FACTORS-------------#
    #-------------------------------------------------#

    Nq=a*Kp
    if fi==0:
        Nc=5.14
    else:
        Nc=(Nq-1)/math.tan(fiR)
    Ngamma=(Nq-1)*math.tan(1.4*fiR)

    #------------BEARING CAPACITY FACTORS-------------#
    #-------------------------------------------------#

    qult=c*Nc*sc*dc + sigmazD*Nq*dq*sq + 0.5*gamma*B*Ngamma*sgamma*dgamma               #kPa
    qall=qult/fs                #kPa

    print(qult,qall,Nc,Nq,Ngamma)

# Meyerhof(3,19,0,0,40,120,1.5,3)

    
    
    
    