from misc import *


A,B = 10000000, 20000000

segment = {" " : [0,0,0,0,0,0,0],
           "0" : [1,1,1,0,1,1,1],
           "1" : [0,0,1,0,0,1,0],
           "2" : [1,0,1,1,1,0,1],
           "3" : [1,0,1,1,0,1,1],
           "4" : [0,1,1,1,0,1,0],
           "5" : [1,1,0,1,0,1,1],
           "6" : [1,1,0,1,1,1,1],
           "7" : [1,1,1,0,0,1,0],
           "8" : [1,1,1,1,1,1,1],
           "9" : [1,1,1,1,0,1,1]}

arr = prime_array(B)
i = 0
while(arr[i] < A):
    i += 1
feed = [str(x) for x in arr[i:]]
s, m = 0,0

def diff(arr1,arr2):
    t = 0
    for i in xrange(len(arr1)):
        t += (arr1[i] ^ arr2[i])
    return t
def total_diff(str1, str2):
    transition = 0
    L1,L2 = len(str1), len(str2)
    if(L1 > L2):
        str2 = (L1 - L2) * " "  + str2
    else:
        str1 = (L2 - L1) * " "  + str1
    for i in xrange(max(L1,L2)):
        transition += diff(segment[str1[i]],segment[str2[i]])
    return transition

def digit_sum(string):
    return str(sum([int(s) for s in string]))

for i in xrange(0,len(feed)):
    current = feed[i]
    q = digit_sum(current)
    array = [" ",current]
    while(int(q) != int(current)):
        array.append(q)
        current = q + ""
        q = digit_sum(q)
    array.append(" ")
    for j in xrange(1,len(array)):
        s += 2*sum([sum(segment[x]) for x in array[j]])
        m += total_diff(array[j],array[j-1])
print s-m
