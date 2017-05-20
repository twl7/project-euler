from misc import *

n = 10**9
m = 2*n+1
k = m - n/2
T = (n+1)**2 + n**2
T -= ((n/4+1)*(n+1) + (n/4)*n)
T -= 3*n/4
sq = (n**2)/32
m = math.sqrt(sq)
T += 2*int(math.ceil(m-1))+1
for i in xrange(1,int(m)+1):
    j = math.sqrt(sq-i*i)
    T += 2*(int(math.ceil(j-1))*2+1)
T -= n/4-1
print T
