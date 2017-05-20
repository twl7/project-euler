from misc import *
import Queue

q = Queue.Queue()
n = 100000000

total = 146570273
array = [[3],[4],[5]]

A,B,C = [[1,-2,2],[2,-1,2],[2,-2,3]],\
        [[1,2,2],[2,1,2],[2,2,3]],\
        [[-1,2,2],[-2,1,2],[-2,2,3]]

##q.put(array)
##while(not q.empty()):
##    arr = q.get()
##    s = sum([x[0] for x in arr])
##    if(s <= n):
##        total += n/s
##        for m in [A,B,C]:
##            q.put(m_m(m,arr))

def rec(array):
    global total
    s = sum([x[0] for x in array])
    if(s <= n):
        total += n/s
        for m in [A,B,C]:
            arr = m_m(m,array)
            rec(arr)
limit = int(math.sqrt(n))
for M in xrange(2,limit+1):
    for N in xrange(1,M):
        if(gcd(M,N) == 1):
            if(gcd(M*M-N*N,2*M*N+N*N) == 1):
                P120 = 2*M*M + 3*M*N + N*N
                total += n/P120
            if(gcd(M*M-N*N,2*M*N-N*N) == 1):
                P60 = 2*M*M + M*N - N*N
                total += n/P60
#rec(array)
print total
    
    
