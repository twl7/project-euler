
n = 10**8
arr = range(n+1)
print "ok"
for i in xrange(2,n+1):
    if(i % 1000000 == 0):
        print i
    if(arr[i] == i):
        for j in xrange(i,n+1,i):
            arr[j] = (i-1)*arr[j]/i
print 6*((n*(n+1))/2 - sum(arr))
