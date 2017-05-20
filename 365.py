from misc import *

start = time.time()

N = 10**18
k = 10**9
L, U = 1000,5000

residues = []
primes = prime_range(L,U-L)

def pc(n,p):
    k = 0
    while(n > 0):
        n /= p
        k += n
    return k
        
def modc(n,p):
    neg = 0
    m = 1
    while(n > 0):
        neg ^= (n/p & 1)
        for i in xrange(1,n % p+1):
            m *= i
            m %= p
        n /= p
    return ((-1)**neg * m) % p

def m(n,p):
	t = 1
	for i in xrange(1,n+1):
		while(i % p == 0):
			i /= p
		t = (t * i) % p
	return t

for p in primes:
    if(pc(N,p) - pc(k,p) - pc(N-k,p) == 0):
        residues.append((modc(N,p) * power_mod(modc(k,p),p-2,p) * power_mod(modc(N-k,p),p-2,p)) % p)
    else:
        residues.append(0)

arr = [0] * 3
total = 0
def rec(index,count):
    global arr
    global total
    if(count == 3):
        total += CRT([residues[i] for i in arr],[primes[i] for i in arr],[primes[i]-1 for i in arr])[0]
        return
    if(index < len(primes)):
        rec(index+1,count)
        arr[count] = index
        rec(index+1,count+1)
rec(0,0)
print total
print "Took " + str(time.time()-start)
