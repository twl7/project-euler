from misc import *

start = time.time()
mod = 1000000007
n = 10000000
m = 10010000
arr = [[] for i in xrange(int(math.sqrt(m)+2))]
def G(n):
    global arr
    t = 1
    
    sq = Decimal(n).sqrt()
    N = Decimal(n)
    for i in xrange(sq):
        diff = (i+1) * sq
        k = int(N-diff)
##        if(k < 0):
##            break
        arr[i+1].append(k+i+1)
        #t += nCk_mod(k+i+1,i+1,mod) 
    return t % mod

T = 0
for p in prime_range(n,m-n):
    T += G(p)
print T % mod
print time.time() - start

#581468882
