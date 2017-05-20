from misc import *

start = time.time()
n = 1000000
mod = 100000007
f = factorial = [1]
for i in xrange(1,n+1):
    factorial.append((i*factorial[-1]) % mod)
inverse = [power_mod(F,mod-2,mod) for F in factorial]
total = 0
for i in [0,1,2]:
    factor = 2 if i == 1 else 1
    spaces = n - i
    for seats in xrange(1+(spaces +1)/3, (spaces+3)/2):
        gaps = seats-1
        twos = spaces - seats - gaps
        ones = gaps - twos
        total += factor * f[seats] * power_mod(2,twos,mod) * f[twos+i] * f[ones+twos] * \
            f[ones+twos] * inverse[ones] * inverse[twos]
        total %= mod
        
print total
print time.time()- start
