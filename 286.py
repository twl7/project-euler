from decimal import *

f = 50.0

def pr(q):
    prob = [Decimal(1.0)] + [Decimal(0.0)] * 50
    for distance in xrange(1,51):
        hit = Decimal(1.0) - Decimal(distance)/Decimal(q)
        miss = Decimal(distance)/Decimal(q)
        for i in xrange(50,0,-1):
            prob[i] = hit * prob[i-1] + miss * prob[i]
        prob[0] *= miss
    return prob[20]
increment = 1.0
i = 0
target = Decimal(0.02)
while(i < 12):
    p = pr(f)
    if(p > target):
        f+=increment
    else:
        i += 1
        f -= increment
        increment /= 10

print f
