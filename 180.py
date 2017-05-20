from misc import *

k = 35

def square_root(frac):
    n = int(math.sqrt(frac.numerator))
    d = int(math.sqrt(frac.denominator))
    if(n*n == frac.numerator and d*d == frac.denominator):
        return Fraction(n,d)
    return False
T = Fraction(0,1)
sums = set()
for ad in xrange(2,k+1):
    for an in xrange(1,ad):
        if(gcd(an,ad) == 1):
            A = Fraction(an,ad)
            for bd in xrange(2,k+1):
                for bn in xrange(1,bd):
                    if(gcd(bn,bd) == 1):
                        B = Fraction(bn,bd)
                        i = 0
                        for C in [square_root(1/(A**-2+B**-2)),1/(1/A+1/B),A+B, square_root(A**2+B**2)]:
                            if(C and C.denominator <= k and C.numerator < C.denominator):
                                  #print A,B,C, i
                                  sums.add(str(A+B+C))
                            i += 1
for s in sums:
    T += Fraction(s)
print T.numerator+T.denominator
