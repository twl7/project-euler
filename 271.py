from misc import *


start = time.time()

N = 13082761331670030
i = 2
mods = []
while(N > 1):
    if(N % i == 0):
        t = 1
        while(N % i == 0):
            N /= i
            t *= i
        mods.append(t)
    i += 1
L = len(mods)

residues = []

for mod in mods:
    r = []
    for i in xrange(1,mod):
        if(i**3 % mod == 1):
            r.append(i)
    residues.append(r)
    
arr = [1] * L
total = 0
def rec(index):
    global total
    global arr
    if(index < L):
        for r in residues[index]:
            arr[index] = r
            rec(index+1)
    else:
        total += CRT(arr,mods,[mod-1 for mod in mods])[0]

rec(0)
print total-1
print "Took " + str(time.time() - start)
print 
