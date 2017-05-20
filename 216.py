from misc import *
start =time.time()
n = 5 * 10**7

primes = prime_array(int(math.sqrt(2) * n))
arr = [0] + [1] * n
arr[1] = 0

for p in primes[1:]:
    sq = (p+1)/2
    x = modular_sqrt(sq,p)
    if(x**2 % p == sq):
        y = p-x
        x,y = min(x,y),max(x,y)
        if(x*x == sq):
            x+=p
        for i in xrange(x,n+1,p):
            arr[i] = 0
        for i in xrange(y,n+1,p):
            arr[i] = 0
print sum(arr)
print time.time() - start

#5437849


