from misc import *

start = time.time()

lim = 10**12
A = []
t = []
for a in xrange(40):
    for b in xrange(40):
        for c in xrange(40):
            n = 2**a * 3**b * 5**c
            if(n <= lim):
                A.append(n)
                if(is_prime(n+1)):
                    t.append(n+1)
            else:
                break
A.sort()
sums = [0] * len(A)
for i in xrange(len(A)):
    sums[i] = A[i] + sums[i-1]
t.sort()
t = t[3:]
L = len(t)
T = 0
def rec(prod,index):
    global T
    if(index < L):
        last = min(b_s(t,lim/prod),L-1)
        for i in xrange(index,last+1):
            rec(prod * t[i],i+1)
##        if(prod * t[index] <= lim):
##            rec(prod * t[index],index+1)
##        rec(prod,index+1)   
    T += sums[b_s(A,lim/prod)] * prod
rec(1,0)
print T % (2**32)
print "Took " + str(time.time() - start)
#939087315
