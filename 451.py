from misc import *
start = time.time()
def sr(mods,totients):
    if(len(mods) == 0):
        return 0
    roots = []
    residues = []
    for m in mods:
        if(m == 2):
            residues.append([1])
        elif(m % 8 == 0):
            residues.append([1,m-1,m/2+1,m/2-1])
        else:
            residues.append([1,m-1])
    def rec(arr,index):
        if(index == len(mods)):
            roots.append(CRT(arr,mods,totients)[0])
            
        else:
            for r in residues[index]:
                rec(arr + [r],index+1)
    rec([],0)
    roots.sort()
    i = len(roots)-1
    while(i > 0 and roots[i] == roots[-1]):
        i -= 1
    return roots[i]

n = 20000000
primes = prime_array(int(math.sqrt(n)))
arr = [0] * (n+1)
#total = 0
block = 1000000
for i in xrange(n/block):
    s = 1 + i*block
    mtarr = [[[],[],s+z] for z in xrange(block)]
    for p in primes:
        index = ((s+p-1)/p) * p -s
        for j in xrange(index,block,p):
            mtarr[j][2] /= p
            mtarr[j][0] += [p]
            mtarr[j][1] += [p-1]
            while(mtarr[j][2] % p == 0):
                mtarr[j][2] /= p
                mtarr[j][0][-1] *= p
                mtarr[j][1][-1] *= p
    for j in xrange(block):
        if(mtarr[j][2] != 1):
            mtarr[j][0] += [mtarr[j][2]]
            mtarr[j][1] += [mtarr[j][2]-1]
        arr[s+j] = sr(mtarr[j][0],mtarr[j][1])
##for i in xrange(3,n+1):
##    mods = []
##    totients = []
##    for p in primes:
##        if(i % p == 0):
##            i/=p
##            mods += [p]
##            totients += [p-1]
##            while(i % p == 0):
##                i /= p
##                mods[-1] *= p
##                totients[-1] *= p
##    if(i != 1):
##        mods.append(i)
##        totients.append(i-1)
##    a = sr(mods,totients)
##    total += a
print sum(arr[3:])
print time.time() - start
