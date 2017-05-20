from misc import *
import time

m = time.time()
n = 600000000
divisors = [1] * (n+2)
for i in xrange(2,n+2):
    for j in xrange(i,n+2,i):
        divisors[j] += 1
print time.time()-m
a = divisors[n+1]
for i in xrange(n+1,1,-1):
    if(i % 2 == 0):
        divisors[i] = divisors[i/2] * a
    else:
        a = divisors[i]
        divisors[i] *= divisors[(i+1)/2]
for i in xrange(n+2):
    divisors[i] = [divisors[i],0,0]

##arr = [divisors[0][0]]
##index = 0
##for i in xrange(2,n):
##    while(index > 0 and divisors[i][0] >= arr[index]):
##            arr.pop()
##            index -= 1
##    index += 1
##    arr.append(divisors[i][0])
##    divisors[i][1] = index
##
##arr = [divisors[n][0]]
##index = 0
##for i in xrange(n,0,-1):
##    while(index > 0 and divisors[i][0] < arr[index]):
##            arr.pop()
##            index -= 1
##    index += 1
##    arr.append(divisors[i][0])
##    divisors[i][2] = index

t = 0
for i in xrange(2,n):
    t += divisors[i][1] * divisors[i][2]
print t
