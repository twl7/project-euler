import misc
n = 10**8
arr = misc.primality_array(n)
t = 0
for p in xrange(5,n,2):
    if(p % 1000000 == 0):
        print p/1000000
    if(arr[p]):
        s = 0
        mod = 1
        for k in [2,3,4]:
            mod = (misc.power_mod(p-k,p-2,p) * mod) % p
            s += mod
        t += s % p
            
print t
