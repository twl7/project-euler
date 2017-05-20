from misc import *
n = 10**6
mod = 10**9 + 7
t = 0
for k in xrange(1,n+1):
    v = (1-k**2) % mod
    t += (power_mod(v,n+1,mod) - v) * power_mod(v-1,mod-2,mod)
print t % mod

#191541795
