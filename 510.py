from misc import *

n = 10**15
T = 0
for b in xrange(1,int(n**0.25)+1):
    for a in xrange(1,b+1):
        
        if(gcd(a,b) == 1):
            A,B = a**2,b**2
            mult = (a+b)**2
            k = n/(B*mult)
            s = (A+B)*mult + A*B
            T += (k*(k+1) * s)/2
print T
            
            
