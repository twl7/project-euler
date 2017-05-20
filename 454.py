from misc import *

start = time.time()

n = 10**12
total = 0

limit = int(math.sqrt(n))
primes = [[]] + [[] for i in xrange(limit)]
for p in xrange(2,limit+1):
    if(len(primes[p]) == 0):
        for i in xrange(p,limit+1,p):
            for j in xrange(len(primes[i])):
                primes[i].append(primes[i][j] * -p)
            primes[i].append(p)
for P in primes:
    P.reverse
maximum = [0] * (limit+1)
for i in xrange(2,limit+1):
    y = n/i
    if(i <= y/(i+1)):
        for j in xrange(1,i):
            if(gcd(i,j) == 1):
                total += y/(i+j)
    else:
        L = 0
        for val in xrange(y/(i+1),max(0,y/(2*i-1)-1),-1):
            u = min(y/val-i,i-1)
            sub = 0
            for p in primes[i]:
                if(p > 0):
                    sub += u/p
                else:
                    sub -= u/(-p)
            u -= sub
            total += (u-L)*val
            L = u
                
print total
            





print time.time() -start
