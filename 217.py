
n = 47
mod = 3**15
L = 9*(max(n/2,1)) + 1
without_zero = []
with_zero = []
sums = [without_zero, with_zero]
for j in xrange(2):
    
    for i in xrange(max(n/2,1) + 1):
        sums[j].append([0] * L)
    sums[j][0][0] = 1
        
for i in xrange(10):
    with_zero[1][i] = 1
    if(i != 0):
        without_zero[1][i] = 1

for j in xrange(2):
    for i in xrange(2,len(sums[0])):
        for s in xrange(L):
            for d in xrange(min(9,s)+1):
                sums[j][i][s] += sums[j][i-1][s-d]
            sums[j][i][s] %= mod
for j in xrange(2):
    sums[j].append([0] * L)
    
total = 45
for digits in xrange(2,n+1):
    sides = digits/2
    t = 10**sides
    right_mul = t/9
    left_mul = t*(right_mul/10)
    end = 10**(digits-1)
    factor = 1
    if(digits & 1 == 1):
        left_mul *= 10
        factor = 10
    for d in xrange(1,10):
        #left
        for ds in xrange(d,L):
            total += (factor*left_mul*d*without_zero[sides-1][ds-d]*with_zero[sides][ds]) % mod
            
            total += (factor*end*d * with_zero[sides-1][ds-d]*with_zero[sides][ds]) % mod
        #middle
        if(digits & 1 == 1):
            for ds in xrange(L):
                total += (d*t*without_zero[sides][ds]*with_zero[sides][ds]) % mod
        
        #right
        for ds in xrange(d,L):
            total += (factor*right_mul*d*without_zero[sides][ds]*with_zero[sides-1][ds-d]) % mod
    total %= mod        
    
    
print total % mod

    
    
