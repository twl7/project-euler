from misc import *

def new_square(A,B):
    [a,b],[c,d] = A,B
    return sorted([a*c + b*d,abs(a*d-b*c)])

n = 150

primes = [y for y in prime_array(n) if y % 4 == 1]
sq = []
for p in primes:
    for i in xrange(1,int(math.sqrt(p/2))+1):
        k = math.sqrt(p - i*i)
        if(k == int(k)):
            sq.append([i,int(k)])
total = 0
def rec(arr,index):
    global total
    if(index < len(sq)):
        rec(arr+[],index+1)
        [a,b] = sq[index]
        rec(new_square(arr,[a,b]),index+1)
        if(sum(arr) != 1):
            rec(new_square(arr,[b,a]),index+1)
        
    else:
        total += arr[0]

rec([0,1],0)   
print total
