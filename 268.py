from misc import *

start =time.time()

N = 10**16
limit = 100

arr = prime_array(100)
total = 0
coe = [0] * 26
coe[4] = 1
for i in xrange(5,26):
	coe[i] = 1
	for j in xrange(4,i):
		coe[i] -= coe[j] * nCk(i,j)

def rec(prod,count,index):
    global total
    if(index < len(arr)):
        if(prod <= N):
            rec(prod,count,index+1)
            rec(prod*arr[index],count+1,index+1)
    else:
        if(count >= 4):
            total +=  (N/prod) * coe[count]

rec(1,0,0)
print total




print "Took " + str(time.time()-start)
