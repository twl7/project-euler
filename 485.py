from misc import *

start = time.time()

n = 10**8
k = 10**5
divisors = [1] * (n+1)
ws = 1
we = 0
for d in xrange(2,n+1):
    for N in xrange(d,n+1,d):
        divisors[N] += 1
T = 0
def add(index):
    global divisors, ws, we
    while(we >= ws and divisors[index] >= divisors[we][0]):
        divisors[we] = 0
        we -= 1
    we += 1
    divisors[we] = [divisors[index],index]
    
    while(divisors[ws][1] <= index-k):
        ws+=1
            
for i in xrange(k):
    add(i+1)
T = divisors[ws][0]
for i in xrange(k+1,n+1):
    add(i)
    T += divisors[ws][0]

print T

print time.time() - start
