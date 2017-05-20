import misc
import math
n = 10**8
p = misc.primality_array(n)

##def pgen(array):
##    def ans(a,b,arr):
##        if(len(arr) == 0):
##            return p[a+b] == 1
##        else:
##            return ans(a*arr[0],b,arr[1:]) and ans(a,b*arr[0],arr[1:])
##    return ans(1,1,array)

s = 1
for i in xrange(2,n,2):
        m = False
        if(p[i+1] and p[(i/2) +2]):
            m = True
            for sq in xrange(2,int(math.sqrt(i))):
                    if(i % sq == 0 and not p[i/sq + sq]):
                        m = False
                        break
        if(m):
            s += i
print s
