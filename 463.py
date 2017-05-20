from misc import *

n = 3**37

bits = []
k = n
while(k > 0):
    bits.append(k & 1)
    k >>= 1
L = len(bits)
values = [0] * L
values[0] = n
for i in xrange(L-1):
    for j in xrange(i):
        values[i-j] += 1 << (i-1)
k = n - (1 << (L-1))


for i in xrange(L-1):
    if(bits[i] == 1):
        values[L-1-i] += ((k & ((1 << i) -1))+1)
    values[L-1-i] += (k >> (i+1)) << i

print sum([(2**i) * values[i] for i in xrange(L)])
