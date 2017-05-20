from misc import *
import math

start = time.time()
n = 100000000#10**8
pr = primality_array(n)

for i in xrange(n,2,-1):
    if(pr[i-1]):
        pr[i-1] -= 1
        pr[i] += 1

t = 0
sq = int(math.sqrt(n))
for s in xrange(2,sq+1):
    arr = []
    squ = []
    for i in xrange(1,s):
        if(gcd(i,s) == 1):
            arr.append(i)
            squ.append(i**2)

    L = len(arr)
    Q = s*s
    for i in xrange(Q,n+1,Q):
        if(pr[i]):
            for j in xrange(L):
                x = squ[j]*i/Q
                if(pr[x]):
                    y = arr[j]*i/s
                    if(pr[y]):
                        t += (x+y + i)-3
        
print t
print time.time() - start


#100315739184392
