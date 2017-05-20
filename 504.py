from misc import *

p = [0,0,0,0]
a,b,c,d = 0,0,0,0
t = 0
gcds = [[0 for i in xrange(101)] for j in xrange(101)]
for a in xrange(1,101):
    for b in xrange(1,101):
        gcds[a][b] = gcd(a,b)
for i in xrange(10**8):
    if(i % 1000000 == 0):
        print i/1000000
    for j in xrange(4):
        p[j] = 1 + (i % 100)
        i/= 100
    [a,b,c,d] = p
    interior = ((a+c)*(b+d) +2 -  gcds[a][b] -gcds[b][c] -  gcds[c][d]- gcds[d][a])/2
    d = int(math.sqrt(interior))
    if(d*d == interior):
        t += 1
print t
    
    
