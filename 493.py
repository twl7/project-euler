from misc import *

values = [combinations(10*i,20) for i in xrange(8)]

for i in xrange(3,8):
    for j in xrange(2,i):
        values[i] -= values[j] * combinations(i,j)
t = 0
for i in xrange(2,8):
    t += i * values[i] * combinations(7,i)

print Decimal(t)/Decimal(combinations(70,20))
