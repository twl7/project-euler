from misc import *

start = time.time()

n = 10**7
pt = [0] * (n+1)
calc = [0] * (n+1)
for i in xrange(9):
    calc[i] = 1
for i in xrange(3,n+1):
    
    d = i**2
    if(d & 1 == 1):
        d+= 6*i+9
##    div = d/48
##    rem = d % 48
##    if(rem > 24 or rem == 24 and div & 1 == 1):
##        div += 1
    pt[i] = int(round(float(d)/48.0))
print pt[n]
for i in xrange(3,n/2+1):
    for j in xrange(2*i,n+1,i):
        pt[j] -= pt[i]

def f(x):
    global pt, calc
    
    if(x > n):
        return 0
    if(calc[x] == 0):
        for den in xrange(2,int(math.sqrt(x))):
            pt[x] -= pt[x/den]
        for div in xrange(3,int(math.sqrt(x))+1):
            pt[x] -= (x/div - x/(div+1)) * pt[div]
        
        calc[x] = 1
    return pt[x]

print sum(pt)
print time.time() -start
