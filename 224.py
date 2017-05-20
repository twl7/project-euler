from misc import *

start = time.time()
def new_square(A,B):
    [a,b],[c,d] = A,B
    return sorted([a*c + b*d,abs(a*d-b*c)])

n = 75000000
c = n/2
arr = [0] * (c+1)
for i in xrange(2,c+1,2):
    arr[i] = []

t = 0
for i in xrange(1,int(math.sqrt(c)) +1):
    for j in xrange(i+1):
        d = i**2 + j**2
        if(d <= c and d & 1 == 0):
            arr[d].append([j,i])

for i in xrange(3,c+1,2):
    squares = []
    for a in arr[i-1]:
        for b in arr[i+1]:
            squares.append(new_square(a,b))
            squares.append(new_square(a,[b[1],b[0]]))
    squares.sort(key = lambda x: x[0])
    last = -1
    for x in squares:
        if(x[0] == last):
            continue
        last = x[0]
        if(x[0] + x[1] > i and x[0] + x[1] + i <= n):
            t+=1
            
    

print t
print time.time() - start


#4137330

