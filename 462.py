from misc import *

def smooth(n):
	arr = []
	e2, e3 = 0, 0
	while(3**e3 <= n):
		e2 = 0
		while(2**e2 * 3**e3 <= n):
			e2 +=1
		arr.append(e2)
		e3 += 1
	return arr

n = 10**18
arr = smooth(n)
L = len(arr)

d = Decimal(1.0)
for i in xrange(1,sum(arr)+1):
        d *= i
arr.append(0)
for i in xrange(L):
        b = arr[i]
        for j in xrange(i+1,L+1):
                for diff in xrange(arr[j-1] - arr[j]):
                        #print i, (b-arr[j]-diff-i+j-1)
                        d /= (b-arr[j]-diff-i+j-1)

print d
                

#5.5350769703e1512
