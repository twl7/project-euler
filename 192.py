import fractions
import math
import time
from decimal import *
F = fractions.Fraction

start = time.time()
def arr_to_cf(arr):
    if(len(arr) == 0):
        return F(0,1)
    if(len(arr) == 1):
        return F(arr[0],1)
    return F(arr[0],1) + 1/arr_to_cf(arr[1:])

n = 10
lim = 10**12
t = 0

def ba(i,lim):
    sq = Decimal(math.sqrt(i))
    
    num, den = [Decimal(1.0),Decimal(0.0)],[Decimal(0.0),Decimal(1.0)]
    arr = []
    while(arr_to_cf(arr).denominator <= lim):
        c = int((num[0] * sq + num[1])/(den[0]*sq + den[1]))
        arr.append(c)
        num[0] -= c*den[0]
        num[1] -= c * den[1]
        num,den = den,num
    low,hi = 0,0
        
    return arr_to_cf(arr).denominator
for i in xrange(2,n+1):
    sq = Decimal(math.sqrt(i))
    if(sq != int(sq)):
        num, den = [Decimal(1.0),Decimal(0.0)],[Decimal(0.0),Decimal(1.0)]
        arr = []
        while(arr_to_cf(arr).denominator <= lim):
            c = int((num[0] * sq + num[1])/(den[0]*sq + den[1]))
            arr.append(c)
            num[0] -= c*den[0]
            num[1] -= c * den[1]
            num,den = den,num
        
        t += arr_to_cf(arr[:-1]).denominator

print t
print time.time() - start
