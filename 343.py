from misc import *



start = time.time()

n = 2000

p = prime_array(n)
def L(m):
    d = math.sqrt(m)
    for i in p:
        if(i > d):
            break
        while(m % i == 0):
            m /= i
        if(m == 1): return i
    return m
t = 21197996132102413
s = 839275
for i in xrange(s,n+1):
    t += max(L(i+1),L(i**2-i+1))
print t - n

print time.time() -start
