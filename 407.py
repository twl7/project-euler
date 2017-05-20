from misc import *

start = time.time()
n = 10**7
arr = [[] for i in xrange(n+1)]
for i in xrange(2,n+1):
    if(len(arr[i]) == 0):
        for j in xrange(i,n+1,i):
            arr[j].append(i)
total = 0
for i in xrange(2,n+1):
    L = len(arr[i])
    mods, totients = [],[]
    for prime in arr[i]:
        k = i
        mod = 1
        while(k % prime == 0):
            k /= prime
            mod *= prime
        mods.append(mod)
        totients.append((prime-1) * mod / prime)
    m = 0
    for j in xrange(2**L):
        residues = [(j >> place) & 1 for place in xrange(L)]
        m = max(m,CRT(residues,mods,totients)[0])
    total += m
print total





print "Took {0:4f}".format(time.time()- start)
