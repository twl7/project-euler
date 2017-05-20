from misc import *

n = 10**10

area = lambda x,y : int(math.sqrt(4*x*x*y*y + x*x+y*y))
T = 0
c = 0
d = dict()
for k in xrange(1,int(math.sqrt(n))+1):
    #x^2 + y^2 = 4kxy + k^2
    x,y = k,0
    while(True):
        x,y = 4*k*x-y,x
        A = area(x,y)
        
        if(A <= n):
            d[n*x+y] = A
            c+=1
            #print x,y,A
            T += A
        else:
            break
    # x^2 + y^2 = -4kxy + k^2
    # k = 2xy +- area 
    
print c,T
            
    
