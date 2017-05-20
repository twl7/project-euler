from misc import *


start = time.time()
a,b,c = 21**7,7**21,12**7
def F(n):
    if(n > b):
        return n-c
    else:
        return F(a + F(a + F(a + F(a + n))))

def S(a,b,c):
    
    diff = a-c
    cycles = (b+1)/a
    summation = 3*cycles*(cycles+1)/2 + cycles
    partial = b%a 
    T = b*(b+1) + diff * summation * a - cycles * a * (a-1)/2
    T += diff * (3*cycles + 4) * (partial+1) - partial*(partial+1)/2
    return T


print S(a,b,c)

print time.time() -start
