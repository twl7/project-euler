from misc import *

n = 10**12
mod = 10**8
d = {0b1001 : 0, 0b1100 : 1, 0b0011 : 2,
     0b0110 : 3,
     0b11001: 4, 0b11100 : 5, 0b10011 : 6}
starting = [0b1100,0b0110, 0b0011, 0b11001]
ending = [0b1001,0b11001]

trans = [[0,1,1,1,0,1,1],
         [1,0,0,0,1,0,0],
         [1,0,0,0,1,0,0],
         [1,0,0,0,0,0,0],
         [1,0,0,0,1,0,0],
         [0,1,0,0,0,1,0],
         [0,0,1,0,0,0,1]]

arr = [0] * len(d)
for p in starting:
    arr[d[p]] = 1

trans = m_e(trans,n-2,mod)

arr = [e[0] for e in m_m(trans,[[a] for a in arr])]

print sum([arr[d[e]] for e in ending]) % mod



