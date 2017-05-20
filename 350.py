from misc import *

G, L, N = 10**6,10**12,10**18
mod = 101**4
powers = [power_mod(i,N,mod) for i in xrange(21)]
combo = [0,1]
for i in xrange(2,21):
    combo.append((powers[i] - 2*powers[i-1] + powers[i-2]) % mod)

seq = [1] * (L/G + 1)
div = len(seq)
for i in xrange(2,div):
    if(seq[i] == 1):
        for j in xrange(i,div,i):
            m = j
            d = 0
            while(m % i == 0):
                m /= i
                d+=1
            seq[j] *= combo[d+1]
            seq[j] %= mod
t = 0
for i in xrange(1,div):
    t += seq[i] * (L/i - G + 1)
    t %= mod
print t
