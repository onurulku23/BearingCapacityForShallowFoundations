import math

def Terzaghi(shape,h,gamma,c,fi,B,Df,fs):

    g=9.81

    fiR=fi*math.pi/180
    
    a=math.exp(math.pi*(3/4-fi/360)*math.tan(fiR))
    
    # Kp=math.tan((math.pi/4)+(fiR/2))**2
    
    gamma1=gamma                    #for Zw>=B      Zw=h-Df
    gamma2=gamma-g+((h-Df)/B)*g     #for 0<Zw<B
    gamma3=gamma-g                  #for Zw<=0
    
    Nq=(a**2)/(2*(math.cos((math.pi/4)+fiR/2))**2)
    
    if fi==0:
        Nc=5.7
    else:
        Nc=(Nq-1)*(math.cos(math.radians(fi))/math.sin(math.radians(fi)))
    
    NgammaDict={"0":0.00,"1":0.01,"2":0.04,"3":0.06,"4":0.10,"5":0.14,
            "6":0.20,"7":0.27,"8":0.35,"9":0.44,"10":0.56,"11":0.69,
            "12":0.85,"13":1.04,"14":1.26,"15":1.52,"16":1.82,"17":2.18,
            "18":2.59,"19":3.07,"20":3.64,"21":4.31,"22":5.09,"23":6.00,
            "24":7.08,"25":8.34,"26":9.84,"27":11.60,"28":13.70,"29":16.18,
            "30":19.13,"31":22.65,"32":26.87,"33":31.94,"34":38.04,"35":45.41,
            "36":54.36,"37":65.27,"38":78.61,"39":95.03,"40":116.31,"41":140.51,
            "42":171.99,"43":211.56,"44":261.60,"45":325.34,"46":407.11,"47":512.84,
            "48":650.67,"49":831.99,"50":1072.80
            }
    Ngamma=NgammaDict[str(fi)]

    if shape=="Square Footing":
        sc=1.3
        sgamma=0.8
    elif shape=="Strip Footing":
        sc=1
        sgamma=1
    elif shape=="Circular Footing":
        sc=1.3
        sgamma=0.6
    
    Cf=sc*Nc*c

    if Df<h:
        Qf=gamma*Df*Nq
    else:
        Qf=(gamma*h+(Df-h)*(gamma-g))*Nq
    
    if h-Df>=B:
        Gf=0.5*sgamma*gamma1*B*Ngamma
    elif h-Df<=0:
        Gf=0.5*sgamma*gamma3*B*Ngamma
    elif h-Df<B:
        Gf=0.5*sgamma*gamma2*B*Ngamma

    qult=Cf+Qf+Gf       #kPa
    qall=qult/fs        #kPa
    print(qult,qall,Nc,Nq,Ngamma)

# Terzaghi("Strip Footing",3,19,0,33,40,1.5,3)

