from misc import *

start = time.time()
x_lim = 100
n = 10**15
mod = 15
mods,totients = [],[]

for i in xrange(2,mod+1):
    if is_prime(i):
        mods.append(i**multiplicity(mod,i))
        totients.append(mods[-1]*(i-1)/i)

T = 0
for x in xrange(1,x_lim+1):
    residues = []
    for m in mods:
        if(gcd(x,m) == 1):
            terms = [0,x % m, (x*x) %m]
            while((terms[-2],terms[-1]) != (terms[0],terms[1])):
                terms.append((x*x*terms[-2] + x*terms[-1]) % m)
            L = len(terms)-2
            s = sum(terms)-x
            residues.append(((n+1)/L * s + sum(terms[:(n+1) % L]) % m))
        else:
            terms = [0,x % m]
            while(terms[-1] != 0):
                terms.append((x*x*terms[-2] + x*terms[-1]) % m)
            residues.append(sum(terms))



    arr = CRT(residues,mods,totients)
    T = (T + arr[0]) % arr[1]
    

print T
print time.time() - start
