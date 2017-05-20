from misc import *
n = 10
def area(a,b,c): 
    return math.sqrt((a+b+c)*a*b*c)
def area2(a,b,c):
    return math.sqrt((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))/4.0

zero = 0.0
covered = zero
iteration = 40
R,r = 1.0, 1.0/(1+2/math.sqrt(3))

def radius(radii,inner):
    [a,b,c] = sorted(radii)
    #print a,b,c
    m = 0
    if(inner):
        A = area(a,b,c)
        hi,lo = c,zero
        for i in xrange(iteration):
            m = (hi+lo)/2
            val = area(a,b,m) + area(a,m,c) + area(m,b,c)
            if(val < A):
                lo = m
            else:
                hi = m
    
    else:
        #   a+m ^2 - c-a^2 -c-m^2  / 2c-ac-m = cos
        #A = area2(c-a,c-b,a+b)
        A = math.acos(((c-a)**2+(c-b)**2 - (a+b)**2)/(2*(c-a)*(c-b)))
        hi,lo = a,zero
        for i in xrange(iteration):
            m = (hi+lo)/2
            #val = area2(c-a,c-m,a+m) + area2(c-b,c-m,b+m) - area(m,a,b)
            val = math.acos(((c-a)**2+(c-m)**2 - (a+m)**2)/(2*(c-a)*(c-m))) + \
                  math.acos(((c-m)**2+(c-b)**2 - (m+b)**2)/(2*(c-m)*(c-b)))
            if(val < A):
                lo = m
            else:
                hi = m
    return m     
        
def rec(radii,inner,k,scale):
    global covered
    
    if(min(radii) < 0.1):
        scale *= 10.0
        radii = [10.0*r for r in radii]
    [a,b,c] = sorted(radii)
    if(k > 0):
        r = radius(radii,inner)
        #print r,k
        covered += (r/scale)**2
        rec([a,r,c],inner,k-1,scale)
        rec([r,b,c],inner,k-1,scale)
        rec([a,b,r],True,k-1,scale)

rec([r,r,R],False,n,1.0)
covered *= 3
rec([r,r,r],True,n,1.0)
covered += 3*r*r
print 1-covered

        
        
