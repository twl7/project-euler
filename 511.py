from misc import *


n,k = 1234567898765,4321
mod = 10**9
factors = [1]
pf = []
m = n
for i in xrange(2,1000000):
    while(m % i == 0):
        m /= i
        pf.append(i)
for prime in pf:
    l = len(factors)
    for f in xrange(l):
        factors.append((factors[f]*prime) % k)
arr = [0]*k
for f in set(factors):
    arr[f] += 1
        
start = [0]*k
start[0] = 1

def convolute(arr1,arr2,mod):
    L = len(arr1)
    new = [0] * L
    for i in xrange(L):
        for j in xrange(L):
            new[(i+j) % L] += arr1[i]*arr2[j]
    if(mod > 0):
        for i in xrange(L):
            new[i] %= mod
    return new
m = n
while(m > 0):
    if(m % 2 == 1):
        start = convolute(start,arr,mod)
    m /= 2
    arr = convolute(arr,arr,mod)
print start[(-n % k)-k]
            
     

