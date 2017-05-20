from misc import *

start = time.time()

n = 25000000
a = n/3

arr = [0] * (a+2)
for i in xrange(1,a+2,2):
    arr[i] = []

for i in xrange(1,a+2,2):
    for j in xrange(i,a+2,2*i):
        arr[j].append(i)
        #arr[j] += 1
t = (n-1)/2
##for i in xrange(2,a+1):
##    L = i-1
##    H = i+1
##    p = L*H
##    two = 0
##    while(L & 1 == 0):
##        L >>= 1
##        two += 1
##    while(H & 1 == 0):
##        H >>= 1
##        two += 1
##    t += arr[L]*arr[H] * max(two-1,1)

for i in xrange(2,a+1):
    
    L = i-1
    H = i+1
    p = L*H
    two = 0
    while(L & 1 == 0):
        L >>= 1
        two += 1
    while(H & 1 == 0):
        H >>= 1
        two += 1
    if(two == 0):
        for d1 in arr[L]:
            for d2 in arr[H]:
                d = d1*d2
                D = p/d
                if(d > D):
                    break
                c,b = (D+d)/2,(D-d)/2
                if(i <= b and i+b > c and i+b+c <= n):
                    t+=1
    else:
        for d1 in arr[L]:
            for d2 in arr[H]:
                for T in xrange(1,two):
                    d = d1*d2*(2**T)
                    D = p/d
                    if(d > D):
                        break
                    c,b = (D+d)/2,(D-d)/2
                    if(i <= b and i+b > c and i+b+c <= n):
                        t+=1
                
        
print t
print time.time() - start

#61614848
