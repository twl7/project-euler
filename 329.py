from misc import *

total = 0
N = 500
croak = 'PPPPNNPPPNPPNPN'
arr = primality_array(N+1)

def path(t,d,pos,jump):
    global total
    if(arr[pos] == 1 and croak[jump] == 'P'):
        t *= 2
    if(arr[pos] == 0 and croak[jump] == 'N'):
        t *= 2
    if(jump == len(croak)-1):
        total += (t * (2**d))
    else:
        if(pos == 1):
            path(t,d+1,pos+1,jump+1)
        elif(pos == N):
            path(t,d+1,pos-1,jump+1)
        else:
            path(t,d,pos+1,jump+1)
            path(t,d,pos-1,jump+1)
for i in xrange(1,N+1):
    path(1,0,i,0)
denominator = 2**14 * 3**15 * N
g = gcd(denominator,total)
print total/g
print denominator/g
            
