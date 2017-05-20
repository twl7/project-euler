from misc import *
mod = 17**7
totient = 17**6 * 16
i3 = euler_inverse(3,mod)
base,exp = 10,10**18

T = 0

#f[i] = sum 1,n   4**(n-i)  * 4*(2**(i-1)/3) + 2*((2**i)/3)
m = power_mod(2,power_mod(base,exp,totient),mod)
T += 4*m*(m-1)
print T % mod
T -= 42 * (power_mod(16,power_mod(base,exp-1,totient)*(base/2),mod)-1) * euler_inverse(15,mod)
T *= i3
T %= mod

print T
##f = [0] * 1000
##for i in xrange(1,100):
##    f[i] = 4 * f[i-1] + 4*(2**(i-1)/3) + 2*((2**i)/3)
