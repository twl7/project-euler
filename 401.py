import math

n = 10**15
mod = 10**9
def sum_sq(n):
    return (2*n+1) * (n+1) * n /6
sq = int(math.sqrt(n))
t = 0
for i in xrange(1,sq):
    t += i*(sum_sq(n/i) - sum_sq(n/(i+1)))
    t %= mod
for i in xrange(1,n/sq+1):
    t += (n/i) * i**2
    t %= mod
print t
