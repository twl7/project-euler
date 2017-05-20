from misc import *
start = time.time()

n = 5*10**8

primes = prime_array(int(math.sqrt(n)))[1:]

r = inc_range = 1000000
t = 0
for i in xrange(n/inc_range):
    bottom = i*r+1
    arr = [[1,j + bottom] for j in xrange(r)]
    for p in primes:
        s = ((bottom + p-1)/p) * p - bottom
        if(s & 1 == 1):
            s += p
        for j in xrange(s,r,2*p):
            arr[j][1] /= p
            arr[j][0] *= (p-1)
            while(arr[j][1] % p == 0):
                arr[j][0] *= p
                arr[j][1] /= p
    for j in xrange(r):
        if((bottom + j) & 1 == 1):
            t += arr[j][0] * max(1,arr[j][1]-1)
print t
print time.time()-start
