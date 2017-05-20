from misc import *

start = time.time()

n = 10**10
values = dict()
values[1] = 7
values[0] = 0
def F(n):
    global values
    if(n in values.keys()):
        return values[n]
    else:
        lines = (n+1)**3 -1
        s = int(math.sqrt(n))
        for i in xrange(2,s):
            lines -= F(n/i)
        if(n > n/s > s):
            lines -= F(n/s)
        for i in xrange(1,s+1):
            lines -= F(i) * ((n/i) - (n/(i+1)))
        values[n] = lines
        return lines

F(n)

s = str(values[n])
print s[:9] + s[-9:]    
print time.time()-start
