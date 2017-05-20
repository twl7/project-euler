from misc import *
import gc
start = time.time()
values = [1]#[k**5 for k in xrange(1,31)]

total = 0
for n in values:
    s = set()
    L = 2*n+1
    x,y = 1 % n,1 % n
    
    for i in xrange(L):
        v = n*x + y
        if(v in s):
            break
        s.add(v)
        x = (2*x) % n
        y = (3*y) % n
    arr = list(s)
    s.clear()
    gc.collect()
    arr.sort()
    L = len(arr)
    for i in xrange(L):
        arr[i] = arr[i] % n
    total += LIS(arr)
print total
print time.time() - start
