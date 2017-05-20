from misc import *
n = 2011
T = 0

for q in xrange(1,n+1):
    for p in xrange(q):
        if(p+q <= n):
            Q, P = math.sqrt(q),math.sqrt(p)
            d = Q*Q+P*P-2*P*Q
            if(d < 1.0):
                d = -math.log10(d)
                T += int(math.ceil(float(n)/d))
print T
