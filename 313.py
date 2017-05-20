from misc import *

n = 1000000
p = prime_array(n)[1:]
t = 0
for i in p:
    s = (i*i+13/2)
    n = s % 3
    max_n = s/4
    if(n == 1):
        t += ((max_n - n)/3)
    else:
        t += ((max_n - n)/3 + 1)
print t
    
