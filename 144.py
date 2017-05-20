from misc import *

#4x^2 + y^2 = 100
P1,P2 = (0.0,10.1),(1.4,-9.6)

R = 0


def XYC(segment):
    X = segment[1][1] - segment[0][1]
    Y = -(segment[1][0] - segment[0][0])
    C = X*segment[0][0] + Y*segment[0][1]
    return (X,Y,C)

def intersection(xyc,point):
    #X*x + Y*y = C  ->  y = -X/Y * x + C/Y
    #4x^2 + (X/Y)^2 x^2 - 2XC/Y^2 x + C/Y^2 = 100
    (X,Y,C) = xyc
    x = 2*X*C/(Y**2) / ((X/Y)**2 + 4) - point[0]
    y = x*-X/Y + C/Y
    return [x,y]

def reflection(origin,point):
    #slope y/x is -4x/y
    (x,y) = point
    pt = (x + y,y-4*x)
    (X,Y,C) = XYC([point,pt]) #tangent
    a = -X/Y
    c = C/Y
    (x,y) = origin
    d = (x+(y-c)*a)/(1+a**2)
    ref = (2*d-x,2*d*a-y+2*c)
    return XYC([ref,point])

while( not (abs(P2[0]) < 0.01 and P2[1] > 0)):
    #xyc = XYC(P1,P2)
    pt = intersection(reflection(P1,P2),P2)
    P1,P2 = P2,pt
    R += 1
    if(R < 10):
        print P2, 4*P2[0]**2 + P2[1]**2

print R
    
