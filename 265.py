N = 5
P = 2**N
T = 0
def is_rep(array):
    global T
    if(len(array) == P):
        array += [0] * (N-1)
        s = 0
        curr = 0
        for i in xrange(N-1,2**N + N-1):
            curr = (2*curr+ array[i]) % P
            s += 1 << curr
        if(s == 2**P -1):
            c = 0
            for i in xrange(P):
                c *= 2
                c += array[i]
            T += c
def circle(array, zeros, ones):
    if(zeros >= 1):
        circle(array + [0],zeros-1,ones)
    if(ones >= 1):
        circle(array + [1],zeros,ones-1)
    if(zeros + ones == 0):
        is_rep(array)
        
circle([0]*N + [1], P/2-N,P/2-1)
print T
        
