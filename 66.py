import fractions
import math
import time
from decimal import *
F = fractions.Fraction

n = 1000

def arr_to_cf(arr):
    if(len(arr) == 0):
        return F(0,1)
    if(len(arr) == 1):
        return F(arr[0],1)
    return F(arr[0],1) + 1/arr_to_cf(arr[1:])


def ba(i):
    sq = Decimal(i).sqrt()
    
    num, den = [1,0],[0,1]
    arr = []
    while(arr_to_cf(arr).numerator**2 - i*arr_to_cf(arr).denominator**2 != 1):
        #q = arr_to_cf(arr)
       # print q.numerator,q.denominator, q.numerator**2 - i*q.denominator**2 
        #print ((i*den[0]**2)- den[1]**2)
        #(den[0]*i*num[0] - den[1] * num[1] + sq * (den[0] * num[1] - num[0]*den[1]))
        c = int((den[0]*i*num[0] - den[1] * num[1] + sq * (den[0] * num[1] - num[0]*den[1]))/((i*den[0]**2)- den[1]**2))
        arr.append(c)
        num[0] -= c*den[0]
        num[1] -= c * den[1]
        num,den = den,num
        
    return arr_to_cf(arr).numerator
max_x = 0
max_d = 0
for D in xrange(2,n+1):
    if(math.sqrt(D) == int(math.sqrt(D))):
       continue
    X = ba(D)
    if(X > max_x):
        max_x = X
        max_d = D
print max_d
