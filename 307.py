import math
from decimal import *
n = 1000000
k = 20000
logfact = [0.0]
fact = [Decimal(1.0)]

for i in xrange(1,n+1):
    logfact.append( math.log(float(i)) + logfact[i-1])
    fact.append(Decimal(i)*fact[i-1])

s = Decimal(0.0)
total = k * math.log(n)
for double in xrange(k/2+1):
    single = k - 2*double
    s += fact[n] * fact[k]/fact[single]/fact[double]/fact[n-single-double]/(Decimal(2)**double)/Decimal(n)**k
    #s += math.exp((logfact[n] + logfact[k]) - logfact[single] - logfact[double] - logfact[n-single-double] - double * math.log(2) - total)
print Decimal(1.0) - s
