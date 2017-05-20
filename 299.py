from misc import *

n = 100#10**8

T = 0
for a in xrange(2,n/2,2):
    P = (a*a)/2
    for i in xrange(1,int(P**0.5)+1):
        if(P % i == 0 and (2*a+i+P/i) < n):
            print a+i,a+P/i
            T += 2

##for k in xrange(1,int(n**(0.5))+1):
##    a = 1+2*k*k
##    T += (n-2)/(2*(a + k))
for b in xrange(1,n/2):
    

print T
