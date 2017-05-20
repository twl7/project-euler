from misc import *

m, n = 10000,5000
mod = 76543217
prod = 1
squares = m*m-n*n
diff = m-n
if(mod-1 - squares < squares):
    for i in xrange(squares+1,mod-1):
        prod *= i
        prod %= mod
    prod = euler_inverse(prod,mod)
else:
    for i in xrange(1,squares+1):
        prod *= i
        prod %= mod

d = 1
for i in xrange(1,m+1):
    d *= power_mod(i,(2 * min(i,m-i,diff)),mod)
    d %= mod
for i in xrange(1,2*diff):
    d *= power_mod(i+2*diff,min(i,2*diff-i,diff),mod)
    d %= mod


print (prod * euler_inverse(d,mod)) % mod
