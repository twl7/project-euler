from misc import *


start = time.time()
def new_square(x,y):
    [a,b,c,d] = x+y
    return [abs(a*c-b*d),a*d+b*c]
n = 5**5
mul = 1
lim = 2*n
S = 3*lim
arr = [[] for i in xrange(lim)]
for i in xrange(1,int(math.sqrt(lim))+1):
    for j in xrange(i+1):
        s = i*i + j*j
        if(s < lim):
            arr[s].append([j,i])

for z in xrange(1,n):
    Y = set()
    for x in arr[n-z]:
        for y in arr[n+z]:
            for sq in [new_square(x,y),new_square(x,[y[1],y[0]])]:
                Y.add(sq[0])
                Y.add(sq[1])
    S += 8*(2*sum(Y) + z)
    if(0 in Y):
        S -= 8*(2*max(Y) + z)
##                su = z+sum(sq)
##                c = (sq + [z]).count(0)
##                if(0 in sq):
##                    S += 4*su
##                else:
##                    S += 8*su
for i in xrange(1,n):
    j = math.sqrt(n*n-i*i)
    if(int(j) == j):
        S += 4*(i+j)
    



print mul*S
print time.time()-start


##for i in xrange(0,n):
##	for j in xrange(0,n):
##		if(n*n - j*j-i*i < 0):
##			continue
##		z = math.sqrt(n*n - j*j-i*i)
##		if(int(z) == z):
##			count = (i == 0) + (j == 0) + (z == 0)
##			Q += (2**(3-count)) * (i+j+z)
