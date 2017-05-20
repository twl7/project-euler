from external import *

import math
from decimal import *
from fractions import *
import time
#string

def is_palindrome(s):
    L = len(s)
    for i in xrange(L/2):
        if s[i] != s[L-1-i]:
            return False
    return True

def reverse(s):
    l = ""
    for i in xrange(len(s)-1,-1,-1):
        l += s[i]
    return l


#numerical


def gcd(a,b):
    a = abs(a)
    b = abs(b)
    while(b != 0):
        a,b = b, a % b
    return a
GCD = gcd

def euler_inverse(r, p):
    r %= p
    if(gcd(r,p) > 1):
        return -1
    num = 1
    den = r
    while(den > 1):
        f = 1 + p/den
        num,den = num*f % p, den*f % p
    return num


def is_prime(n):
    if(n < 2):
        return False
    for i in xrange(2, 1 + int(math.sqrt(n))):
        if(n % i == 0):
            return False
    return True

def jacobi(a, n):
    t = 1
    while a != 0:
        while a % 2 == 0:
            a >>= 1
            if n % 8 == 3 or n % 8 == 5: t = -t
        if a < n:
            a, n = n, a
            if a % 4 == 3 and n % 4 == 3: t = -t
        a = (a - n) >> 1
        if n % 8 == 3 or n % 8 == 5: t = -t
    if n == 1: return t
    else: return 0

def mod_sqrt(a, p):
    a = a % p
    if(a == 0):
        return 0

    if p % 8 == 3 or p % 8 == 7:
        return pow(a, (p+1)/4, p)

    elif p % 8 == 5:
        x = pow(a, (p+3)/8, p)
        c = (x*x) % p
        if a == c:
            return x
        return (x * pow(2, (p-1)/4, p)) % p

    else:
        
        # find a quadratic non-residue d
        d = 2
        while jacobi(d, p) > -1:
            d += 1

        # set p-1 = 2^s * t with t odd
        t = p - 1
        s = 0
        while t % 2 == 0:
            t /= 2
            s += 1

        at = pow(a, t, p)
        dt = pow(d, t, p)

        m = 0
        for i in xrange(0, s):
            if pow(at * pow(dt, m), pow(2, s-1-i), p) == (p-1):
                m = m + pow(2, i)

        return (pow(a, (t+1)/2) * pow(dt, m/2)) % p

def lcm(a,b):
    return a*b/gcd(a,b)
LCM = lcm

def multiplicity(factorial, p):
    m = 0
    while(factorial > 0):
        m += factorial/p
        factorial /= p
    return m

def nCk(n,k):
    p = 1
    if (k > n): return 0
    for i in xrange(1,k+1):
        p *= n+1-i
        p /= i
    return p

combinations = combo = nCk

def nCk_mod(n,k, mod):
    p = 1
    if (k >= n): return 0
    den = 1
    for i in xrange(1,k+1):
        p *= (n+1-i)
        den *= i
        den %= mod
        p %= mod
    p *= euler_inverse(den,mod)
    return p % mod

def power_mod(base,exponent,mod):
    result = 1
    while( exponent > 0):
        result *= base**(exponent & 1)
        result %= mod
        base = (base * base) % mod
        exponent >>= 1
    return result

def primality_array(n):
    pr = [1] * (n+1)
    pr[0] = pr[1] = 0
    for i in xrange(2,n+1):
        if(pr[i]):
            for j in xrange(2*i,n+1,i):
                pr[j] = 0
    return pr

def prime_array(n):
    pr = [1] * (n+1)
    pr[0] = pr[1] = 0
    arr = []
    for i in xrange(2,n+1):
        if(pr[i]):
            arr.append(i)
            for j in xrange(2*i,n+1,i):
                pr[j] = 0
    return arr

def prime_range(n,m):
    primes = []
    arr = [1] * (m+1)
    q = int(math.sqrt(n+m))
    for i in xrange(2,q+1):
        for num in xrange((-n % i),m+1,i):
            arr[num] = 0
    for i in xrange(m+1):
        if(arr[i]):
            primes.append(n+i)
    return primes

#number theory
##def CRT(AB1,AB2):
##    [a1,b1,a2,b2] = AB1 + AB2
##    B = b1*b2
##    return None

def CRT(residues,mods,totients):
    L = len(residues)
    
    if(L != len(mods) or L != len(totients) or 0 in mods):
        return [0]
    for i in xrange(L):
        residues[i] %= mods[i]
    P = 1
    for mod in mods:
        P *= mod
    prods = [P/mod for mod in mods]
    multipliers = []
    for i in xrange(L):
        m,p = mods[i],prods[i]
        r = p % m
        mul = residues[i] * power_mod(r,totients[i]-1,m)
        if(mul * r % m != residues[i]):
            return [0]
        multipliers.append(mul)
    return [sum([prods[i] * multipliers[i] for i in xrange(L)]) % P,P]
        
    

#matrix
def matrix_id(length):
    return [[ 1 if r == c else 0 for r in xrange(length)] for c in xrange(length)]

def matrix_sum(a,b):
    R = len(a)
    C = len(a[0])
    return [[a[r][c] + b[r][c] for c in xrange(C)] for r in xrange(R)]

def matrix_difference(a,b):
    R = len(a)
    C = len(a[0])
    return [[a[r][c] - b[r][c] for c in xrange(C)] for r in xrange(R)]  

def matrix_multiply(a,b, mod = 0):
    M = len(a)
    if(M == 0): return []
    P = len(a[0])
    if(len(b) != P or P == 0 or len(b) == 0): return []
    N = len(b[0])
    if(N == 0): return []
    prod = [[0 for i in xrange(N)] for j in xrange(M)]
    for i in xrange(M):
        for j in xrange(N):
            for L in xrange(P):
                prod[i][j] += a[i][L] * b[L][j]
            if(mod >= 2):
                prod[i][j] %= mod
    return prod
m_m = matrix_multiply

def matrix_exponentiation(M,exp,mod):
    L = len(M)
    id_m = [[0 for i in xrange(L)] for j in xrange(L)]
    for i in xrange(L):
        id_m[i][i] = 1
    while(exp > 0):
        if(exp % 2 == 1):
            id_m = matrix_multiply(id_m,M,mod)
        M = matrix_multiply(M,M,mod)
        exp /= 2
    return id_m
    
m_e = matrix_exponentiation

def matrix_inverse(m):
    R = len(m)
    C = len(m[0]) if R > 0 else -1
    
    if(R != C):
        raise Exception()
    L = R
    inv = matrix_id(L)
    for col in xrange(L):
        mult = 0
        R = -1
        for row in xrange(col,L):
            if(m[row][col] != 0):
                mult = m[row][col]
                R = row
                break
        else:
            raise Exception()
        
        m[col],m[R] = m[R],m[col]
        inv[col],inv[R] = inv[R], inv[col]

        for i in xrange(L):
            m[col][i] /= mult
            inv[col][i] /= mult
            
        for r in xrange(L):
            if(r == col):
                continue
            mul = m[r][col]
            for c in xrange(L):
                m[r][c] -= mul * m[col][c]
                inv[r][c] -= mul * inv[col][c]        
    return inv

#other algorithms

def binary_search_index(array,value,low_point = True):
    
    hi = len(array) - 1
    if(hi == -1):
        return -1
    if(value < array[0]):
        return -1
    if(value > array[-1]):
        return hi+1
    lo = 0
    if(low_point):
        while(hi - lo > 1):
            mid = (hi+lo)/2
            if(array[mid] >= value):
                hi = mid
            else:
                lo = mid
        if(array[hi] > value):
            return lo
        return hi
    else:
        while(hi - lo > 1):
            mid = (hi+lo)/2
            if(array[mid] > value):
                hi = mid
            else:
                lo = mid
        if(array[hi] >= value):
            return hi
        return lo
    
b_s = binary_search_index    
     
def convolution(A,B):
    pass

def FFT(A,B):
    
    L = max(len(A),len(B))
    K = 1
    while(K < L):
        K <<= 1
    L = K
    A += [0] *(L-len(A))
    B += [0] *(L-len(B))
    output = [0 for i in xrange(2*L-1)]
    addition = [0 for i in xrange(2*L-1)]
    
    def karatsuba(A_l,A_r,B_l,B_r,to_output):
        
        
        if(L <= 2):
            for i in xrange(L):
                for j in xrange(L):
                    output[i+j] += A[i]*B[j]
            return output
        if(L & 1):
            L+=1
            output += [0,0]
        
        
        index = L/2
        A_L = A[:index+1]
        A_R = A[index+1:]
        B_L = B[:index+1]
        B_R = B[index+1:]
        P1 = FFT(A_L,B_L)
        P3 = FFT(A_R,B_R)
        P2 = FFT([A_L[i] + A_R[i] for i in xrange(index)], [B_L[i] + B_R[i] for i in xrange(index)])
        for i in xrange(L):
            output[i] += P1[i]
            output[i+index] += P2[i] - P1[i] - P3[i]
            output[i+L] += P3[i]
    karatsuba(0,L-1,0,L-1)
    return output

def longest_increasing_subsequence(array):
    L = len(array)
    if(L == 0): return 0
    m = max(array)+1
    s = smallest_value_with_length = [m] * (L+1)
    s[0] = array[0]
    ind = index_of_length = [L] * L
    ind[0] = 0
    for i in xrange(1,L):
        value = array[i]
        index = binary_search_index(s,value,False)
        if(value < s[index+1]):
            s[index+1] = value
            ind[index+1] = i
    return binary_search_index(s,m)
LIS = longest_increasing_subsequence

