from misc import * 
start_time = time.time()
#t = 0
##def rec(length, n):
##    global t
##    if(length == 0):
##        t += 1
##    else:
##        for i in xrange(n):
##            rec(length-1,n)
##        rec(length-1,n+1)
n = 10**12
e = elements = 7
mod = 10**9

def equivalence_class(perm):
    s = ""
    d = dict()
    i = 0
    for e in perm:
        if(not e in d):
            i+=1
            d[e] = i
        s += str(d[e])
    return s

c = configurations = dict()
for i in xrange(e**(e-1)):
    arr = [0] * (e-1)
    for j in xrange(e-1):
        arr[j] = i % e
        i /= e
    ec = equivalence_class(arr)
    if(not ec in c):
        c[ec] = 0
    c[ec] += 1

index = dict()
e_arr = c.keys()
e_arr.sort()
L = len(e_arr)
for i in xrange(L):
    index[e_arr[i]] = i

matrix = [[0] * L for i in xrange(L)]
s = str(e-1)
for E in e_arr:
    i = index[E]
    if(s in E):
        for next_e in xrange(1,e):
            matrix[index[equivalence_class(E[1:] + str(next_e))]][i] += 1
    else:
        for next_e in xrange(1,e+1):
            matrix[index[equivalence_class(E[1:] + str(next_e))]][i] += 1

m = m_e(matrix,n-6,mod)
ic = [configurations[E] for E in e_arr]
print sum([x[0] for x in m_m(m,[[e] for e in ic])]) % mod
print time.time()- start_time  
    
    
            
