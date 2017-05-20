from misc import *

start = time.time()
n = 10**9
m = 10**5
k = 10**5
total = 0
primes = prime_range(n,m)
def d(p,k):
    
    #sum p-1,1   1/i  * (p-i-1 + k-1, p-1-i,  k-1)
    #-1 *(p+k-i-2,k-2)
    # 1/(k-1) - (p+k-2,k-1)/

    return euler_inverse(k-1,p)



for p in primes:
    total += d(p,k)
print total
print time.time() - start

#2422639000800
