from misc import *
import random
import gc
start = time.time()

e = math.e
pi =math.pi
PI = Decimal(pi)
n = 10000

values = []
i = 0
v = e**(float(i)/n)-1
while(v <= pi):
    values.append(v)
    i += 1
    v = e**(float(i)/n)-1
L = len(values)

vals = []
error = pi
total = 0
for i in xrange(L):
    for j in xrange(i+1):
        if(values[i] + values[j] <= pi):
            total += 1
t = 0
for iteration in xrange(10):
    vals = []
    gc.collect()
    limit = total/10
    left = total
    for i in xrange(L):
        for j in xrange(i+1):
            if(values[i] + values[j] <= pi):
                if(random.random() <= float(limit)/left):
                    vals.append([values[i] + values[j],i*i+j*j])
                    limit -= 1
                left -= 1
    vals.sort(key = lambda x: x[0])
    end = len(vals)
    vals.append([2*pi,0])

    
    begin = 0
    while(begin <= end):
        while(vals[begin][0] + vals[end][0] >= pi):
            end -= 1
        if(pi - (vals[begin][0] + vals[end][0]) < error):
            error = pi - (vals[begin][0] + vals[end][0])
            t = vals[begin][1] + vals[end][1]
        if(vals[begin][0] + vals[end+1][0] - pi < error):
            error = vals[begin][0] + vals[end+1][0] - pi
            t = vals[begin][1] + vals[end+1][1]
        begin += 1
print t
        
print time.time() - start
