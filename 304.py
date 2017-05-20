from misc import *
mod = 1234567891011
n = 10**14
m = 35 * 10**5
N = 100000

a = [[0,1],[1,1]]

x = prime_range(n,m)
t = 0
for i in xrange(N):
    t += m_e(a,x[i],mod)[0][1]
    t %= mod
print t
