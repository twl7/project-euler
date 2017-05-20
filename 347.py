import misc

n = 10**7
p = misc.primality_array(n)
arr = [[1] for i in xrange(n+1)]
d = dict()
for i in xrange(2,n+1):
    if(p[i]):
        for j in xrange(i,n+1,i):
            if(len(arr[j]) != 0):
                arr[j].append(i)
                if(len(arr[j]) == 4):
                   arr[j] = []
for i in xrange(2,n+1):
    if(len(arr[i]) == 3):
        d[str(arr[i])] = i
print sum(d.values())
