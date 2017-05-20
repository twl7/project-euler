import math

N = 10**10
a,b = 0,2
num = [[0,2]]
while(a*math.sqrt(5)  + b <= 2 * N):
    a,b = (a+b)/2, (5*a+b)/2
    num.append([a,b])
pal = [ ]
for i in xrange(len(num)-1):
    if(i %2 == 0):
        pal.append([num[i][0]+num[i+1][0],num[i][1] - num[i+1][1]])
    else:
        pal.append([num[i][0]-num[i+1][0],num[i][1] + num[i+1][1]])

total = 1

arr = [[2,[1]]]
for i in xrange(4,len(pal)):
    if(pal[i][0] == -pal[i-3][0]):
        arr.append([(pal[i][1] + pal[i-3][1])/2,[i,i-3]])

def rec(indices,i,s):
    global total
    if(i < len(arr)):
        rec(indices+[],i+1,s)
        m = True
        for index in arr[i][1]:
            if(indices[index] == 1):
                m = False
        if(m):
            for index in arr[i][1]:
                indices[index+1] = 1
                indices[index-1] = 1
            rec(indices+[],i+1,s+arr[i][0])
    else:
        total += s
rec([0] * (len(pal)+2),0,0)


print total
    
#pos, neg = [],[]
##for p in pal:
##    if(p[0] < 0):
##        neg.append(p+[])
##    if(p[0] > 0):
##        pos.append(p+[])
##for n in neg:
##    n[0] = abs(n[0])
##psum = [[0,0]]
##nsum = [[0,0]]
##
##for p in pos:
##    L = len(psum)
##    for i in xrange(L):
##        psum.append([p[0] + psum[i][0],p[1] + psum[i][1]])
##        
##for n in neg:
##    L = len(nsum)
##    for i in xrange(L):
##        nsum.append([n[0] + nsum[i][0],n[1] + nsum[i][1]])
##
##psum.sort(key=lambda p: p[0])
##nsum.sort(key=lambda n: n[0])
##L = len(nsum)
##n = 0
##for p in psum:
##    while(nsum[n][0] < p[0] and n < L-1):
##        n += 1
##    if(nsum[n][0] == p[0]):
##        d = (nsum[n][1] + p[1])
##        if(d % 2 == 1):
##            print d
##            continue
##        d /= 2
##        if(2 <= d and d <= N):
##            total += d
##            if(d+2 <= N):
##                total += (d+2)
