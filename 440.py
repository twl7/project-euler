from misc import *

start = time.time()

def gcdpower(a,b):
    while(a != b and b != 0 and a!=0):
        if(a >= 2*b):
            a %= 2*b
        if(a > b):
            a,b = b,a
        if(2*a >= b):
            a,b = a,2*a-b
        a,b = max(a,b),min(a,b)
    return min(a,b)

n = 2000
matrix = [[10,1],[1,0]]
mod = 987898789
total = 0

gcds = [0]*(n+1)
for a in xrange(1,n+1):
    for b in xrange(1,n+1):
        gcds[gcdpower(a,b)] += 1
for c in xrange(1,n+1):
    matrix = [[10,1],[1,0]]
    #m = m_e(matrix,c,mod)
    if(c % 2 == 0):
        total += gcds[0]
    else:
        total += gcds[0]*10
    for a in xrange(1,n+1):
        matrix = m_e(matrix,c,mod)
        total += (matrix[0][0] * gcds[a])
    
    total %= mod
print total
print time.time()- start
        
