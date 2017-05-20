from misc import *

n = 50
x = [0] * (n+1)
for i in xrange(2,n+1):
    for j in xrange(i-1):
        if(x[j] ^ x[i-2-j] == 0):
            x[i] = 1
