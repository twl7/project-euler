from misc import *

start_time = time.time()
N = 7
lim = 10**N
p = primality_array(lim)
d = dict()
for i in xrange(2,lim):
    if(p[i]):
        d[i] = set()
for prime in d.keys():
    s = str(prime)
    L = len(str(prime))
    for i in xrange(L):
        for digit in xrange(10):
            n = int(s[:i] + str(digit) + s[i+1:])
            if(p[n] and len(str(n)) >= L-1):
                d[n].add(prime)
                d[prime].add(n)
    d[prime].remove(prime)

relatives = [2]

for i in xrange(lim):
    p[i] *= lim
p[2] = 2
for j in xrange(20):
    for prime in relatives:
        for r in d[prime]:
            if(p[r] == lim):
                relatives.append(r)
            p[r] = min(p[r],max(p[prime],prime))
t = 0
for i in xrange(lim):
    if(p[i] and p[i] > i):
        t += i

print t
print "Took {0:f}".format(time.time()-start_time)                    
