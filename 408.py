from misc import *
#import numpy

start = time.time()
n = 10000000
mod = 10**9 + 7
sq = []
row = [[]]
total = 0
for i in xrange(1,int(math.sqrt(n))+1):
    for j in xrange(1,int(math.sqrt(n))+1):
        s = math.sqrt(i**2 + j**2)
        if(s == int(s)):
            row[-1].append(j*j)
    if(len(row[-1])):
        sq.append(i*i)
        row.append([])
if(n in sq):
    row.pop()
else:
    sq.append(n)

R = 0
line = [1] * (n+1)
        
        
print total
print time.time()-start
