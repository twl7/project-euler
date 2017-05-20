from misc import *

mod = 10**9

start = time.time()

d = [0] * 4 + [2,5]
for i in xrange(6,100):
    d.append((d[-3] + power_mod(2,i-4,mod)-1 + power_mod(2,i-3,mod) + d[-4] +d[-5] + power_mod(2,i-5,mod)-1) % mod)


print time.time() - start
