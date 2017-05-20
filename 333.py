from misc import *

n = 1000000
arr = [0]* (n+1)
powers = []
for two in xrange(int(math.log(n,2))+1):
    powers.append([])
    T = 2**two
    for three in xrange(int(math.log(n/T,3))+1):
        powers[-1].append(T*3**three)



def rec(index,s,three):
    global arr
    if(s > n):
        return
    if(index == len(powers)):
        arr[s] += 1
        return
    L = len(powers[index])
    for i in xrange(min(L,three)):
        rec(index+1,s+powers[index][i],i)
    rec(index+1,s,three)
        
rec(0,0,len(powers[0])+1)
total = 0
for p in prime_array(n):
    if(arr[p] == 1):
        total += p

print total
    
