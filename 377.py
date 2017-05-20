from misc import *

start = time.time()
n = 9
mod = 10**9

matrix = [[0 for i in xrange(9)] for j in xrange(9)]
matrix[0] = [1] * 9
for i in xrange(8):
    matrix[i+1][i] = 1

arr = [1] + [2**i for i in xrange(8)]
arr.reverse()
total = 0
def rec(num,sum_d):
    global total
    if(sum_d == 0):
        total += num
        total %= mod
    for i in xrange(1,min(sum_d,9)+1):
        rec(10*num + i, sum_d-i)

rec(0,13)

for i in xrange(2,18):
    
    exp = 13**i - n
    mat = m_e(matrix,exp,mod)
    new_arr = [x[0] for x in m_m(mat,[[i] for i in arr])]
    for i in xrange(1,10):
        total += ((mod-1)/9) * new_arr[i-1]*i
        total %= mod
print total
print time.time()- start
    
