from misc import *

start= time.time()
n = 3*10**8
limit = 5

c = 1
p = 9
mod3 = 0
other = 0
for i in xrange(7,100,6):
    if(is_prime(i)):
        p *= i
        c += 1
    if(c == limit-1):
        mod3 = n/p
    if(c== limit):
        other = n/p
        break


arr = prime_array(mod3)
primes = [p for p in arr if p % 3 == 1 or p == 3]
L = len(primes)
sums = range(other+1)

for p in primes:
    for i in xrange(p,other+1,p):
        sums[i] = 0
for i in xrange(1,other+1):
    #countarr[i] = sums[i] + countarr[i-1]
    sums[i] = sums[i] + sums[i-1]
total = 0
count = 0
def rec(lim,prod,index):
    global count
    global total
    if(lim > 0):
        div = n/prod
        for i in xrange(index,L):
            if(primes[i] > div):
                break
            p = primes[i]
            if(p == 3):
                p *= 3
            while(p <= div):
                rec(lim-1,prod*p,i+1)
                p *= primes[i]
    else:
        if(count < 100):
            print prod
        count += 1
        #count += countarr[n/prod]
        total += sums[n/prod]*prod
        if(prod % 3 != 0 and 3*prod <= n):
            total += 3*prod
            
rec(limit,1,0)
print total
print time.time() - start

    
