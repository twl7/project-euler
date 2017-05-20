from misc import *

n = 10**12
k = 10000

primes = prime_range(2 * 10**9,2000)
total = 0

for p in primes:
    f = (n+1) % p
    mod = 0
    for i in xrange(p-1,n % p,-1):
        mod -= ((f * power_mod(i,k,p) - power_mod(i,k+1,p)) % p)
    mod %= p
    total += mod
print total
