from misc import *
start = time.time()
n = 10**14
mod = 982451653
limit = int(3*math.sqrt(n)/2)
#factorial = [1] * limit
inverse = [1] * limit
inverse[0] = 0
for i in xrange(2,limit):
    #factorial[i] = (factorial[i-1] * i) % mod
    inverse[i] = ((mod/i+1)*inverse[i-mod % i]) % mod
for i in xrange(2,limit):
    inverse[i] = (inverse[i] +  inverse[i-1]) % mod
print time.time() - start
T = 10
fact1 ,fact2 = 0, 6 
for k in xrange(2,limit):
    fact1,fact2 = fact2,((k+2)*fact2) % mod
    lower = (k+2)*(k+1)/2 - 1
    if(lower > n):
        break
    upper = (k+3)*(k+2)/2 - 2
    c = min(upper-1,n)
    T+= (k*fact2 * (inverse[k+2] - inverse[k+2 - (c-lower+1)])) % mod
    if(n >= upper):
        T += k*(fact1*(k+3) * (mod/2 +1)) % mod
print T % mod
print time.time() - start
