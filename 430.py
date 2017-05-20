from misc import *


start = time.time()

n = 10**10
m = 4000

##one = Decimal(1)
##denominator = Decimal(n*n)
##E = Decimal(n)/Decimal(2)
##N = Decimal(n)
##j = (one - Decimal(4*i*(n-i+1))/denominator)**m
##while(j >= Decimal(0.0000001) and i <= n/2):
##    E += j
##    
##    i+=1
##    j = (one - Decimal(4*i*(n-i+1))/denominator)**m
i = 1
one = Decimal(1)
N = float(n)
E = Decimal(N/2.0)
j = (1.0 - float(2*(2*i*(n-i+1)-1))/(N**2))**m
bound = Decimal(0.000000001)
bound = 1e-9
while(j >= bound and i <= n/2):
    E += Decimal(j)
    
    i+=1
    j = (1.0 - float(2*(2*i*(n-i+1)-1))/(N**2))**m
if(n % 2 == 1 and i == n/2+1):
    E += j/2
print E
print time.time()-start
