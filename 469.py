from misc import *
N = 10
E = [1.0] * (N+1)
E[0] = [0.0]
E[2] /= 2
for i in xrange(3,N+1):
    for j in xrange(1,i-1):
        E[i] += 2*E[j]
    E[i] /= i
