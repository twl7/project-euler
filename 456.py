from misc import *
start = time.time()
n = 2000000

x = 1
y = 1
p = [0] * n 
for i in xrange(n):
    x = (1248 * x) % 32323
    y = (8421 * y) % 30103
    p[i] = [x-16161,y-15051]
def div(num,den):
    a,b,c,d = num[0],num[1],den[0],den[1]
    # a+bi * c-di
    return [a*c + b*d, b*c-a*d]

def ptcmp(x,y):
    return (x[1] < 0) - (y[1] < 0) or div(x,y)[1] or (x[0] < 0) - (y[0] < 0)
total = nCk(n,3)

p.sort(cmp = ptcmp)
p = p+p
j = 0
repeats = 0
for i in xrange(n):
    while(div(p[j],p[i])[1] >= 0 ):
        j+=1
    j-=1
    if(div(p[j],p[i])[1] == 0 and div(p[i],p[i-1])[1] != 0):
        k = j
        a, b = 0,0
        while(div(p[j],p[k])[1] == 0):
            k -= 1
            a += 1
        k = i
        while(div(p[k],p[i])[1] == 0):
            k+=1
            b+=1
        repeats += a * nCk(b,2) + b * nCk(a,2)
    total -= nCk(j-i,2)
"""
pi = Decimal(math.pi)
angle = lambda point: math.acos(float(point[0])/math.sqrt(point[0]**2 + point[1]**2))
a = [ Decimal(angle(point)) if point[1] >= 0 else Decimal(2*math.pi- angle(point)) for point in p]
a.sort()
for i in xrange(n):
    a.append(a[i] + 2*pi)
j = 0


for i in xrange(n):
    while(a[j] - a[i] <= pi + Decimal(0.0000001)):
        j += 1
    total -= nCk(j-1-i,2)
"""
print total + repeats/2
print time.time() - start
