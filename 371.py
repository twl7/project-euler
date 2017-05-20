from misc import *
n = 1000
N = float(n)
pairs = n/2-1
with_mid = [0.0] * (pairs+1)
without_mid = [0.0] * (pairs+1)
with_mid[pairs] = 2.0
without_mid[pairs] = 2.0 + (2.0/(pairs+1))
for i in xrange(pairs-1,-1,-1):
    pairs_left = float(pairs-i)
    next_state = 2.0*pairs_left + i+1
    with_mid[i] = N/(next_state) + ((2.0*pairs_left)/(next_state)) * with_mid[i+1]
    
    without_mid[i] = N/(next_state) + (2.0*pairs_left/(next_state)) * without_mid[i+1] + \
    (1.0/(next_state)) * with_mid[i]
print without_mid[0]
