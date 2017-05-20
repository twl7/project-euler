from misc import *

ans = 0

n = 1000000
exp = 1234567890
primes= prime_array(n)
arr = [0] * (n+1)
arr[1] = 1
for p in primes:
    mul = 0
    for i in xrange(p,n+1,p):
        j = i
        while(j % p == 0):
            j /= p
            mul += 1
        big_mul = mul*exp
        j = p
        while((j-1)/(p-1) < big_mul):
            j *= p
        maximum = j
        t = 0
        while(j > 1):
            f = (j-1)/(p-1)
            d = big_mul/f
            t += d*j
            maximum = min(maximum,j+t)
            big_mul -= d*f
            j/=p
        if(big_mul == 0):
            maximum = min(maximum,t)
        arr[i] = max(maximum,arr[i])
        
        
for i in xrange(2,n+1):
    arr[i] = max(arr[i],arr[i-1])
##for i in xrange(10,n+1):
##    minimum = 0
##    for p in primes:
##        if(p > i):
##            break
##        mul = multiplicity(i,p)*exp
##        j = p
##        while((j-1)/(p-1) < mul):
##            j *= p
##        maximum = j
##        t = 0
##        while(j > 1):
##            f = (j-1)/(p-1)
##            d = mul/f
##            t += d*j
##            maximum = min(maximum,j+t)
##            mul -= d*f
##            j/=p
##        if(mul == 0):
##            maximum = min(maximum,t)
##        minimum = max(minimum,maximum)
##    ans += minimum
print sum(arr[10:])
    
