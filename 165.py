from misc import *

start = time.time()

n = 500

class BBS():
    s = 290797
    mod = 50515093
    @staticmethod
    def next():
        s = BBS.s
        BBS.s = (s*s) % BBS.mod
        return BBS.s % 500

    @staticmethod
    def reset():
        BBS.s = 290797

def XYC(segment):
    X = segment[1][1] - segment[0][1]
    Y = -(segment[1][0] - segment[0][0])
    C = X*segment[0][0] + Y*segment[0][1]
    g = GCD(X,GCD(Y,C))
    if(C < 0):
        g *= -1
    return (X/g,Y/g,C/g)

def intersection(L1,L2):
    (X1,Y1,C1),(X2,Y2,C2) = L1,L2
    D = X1*Y2-X2*Y1
    
    if(D == 0):
        return 0
    return (Y2 * C1 - Y1 * C2, -X2 * C1 + X1 * C2,D)
    
arr = [[(BBS.next(),BBS.next()),(BBS.next(),BBS.next())] for i in xrange(n)]
#arr = [[[27,44],[12,32]],[[46,53],[17,62]],[[46,70],[22,40]]]
lines = [XYC(s) for s in arr]
d = {}
for seg in arr:
    for p in seg:
        d[str("{:d},{:d},{:d}".format(p[0],p[1],1))] = 0
T = 0
for i in xrange(n):
    for j in xrange(i+1,n):
        P = intersection(lines[i],lines[j])
        if(P == 0):
            continue
        (X,Y,D) = P
        g = GCD(X,GCD(Y,D))
        if(D < 0):
            g *= -1
        X /= g
        Y /= g
        D /= g
        S = str("{:d},{:d},{:d}".format(X,Y,D))
        prod = [(X - arr[i][0][0]*D) * (X - arr[i][1][0]*D),
           (X - arr[j][0][0]*D) * (X - arr[j][1][0]*D),
           (Y - arr[i][0][1]*D) * (Y - arr[i][1][1]*D),
           (Y - arr[j][0][1]*D) * (Y - arr[j][1][1]*D)]
        if(min(prod[0],prod[2]) < 0 and min(prod[1],prod[3]) < 0):
            T+=1
            if(not S in d):
                d[S] = 1

    
print T
print sum(d.values())
print time.time()-start       
