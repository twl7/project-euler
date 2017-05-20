from misc import *

radius = 50.0
diameter = 2*radius
def swap(arr,i,j):
    if(i >= 0 and j >= 0 and i < len(arr) and j < len(arr)):
        arr[j],arr[i] = arr[i],arr[j]
def length(arr):
    L = arr[0] + arr[-1]
    for i in xrange(len(arr)-1):
        L += math.sqrt((arr[i] + arr[i+1])**2 - (diameter-arr[i]-arr[i+1])**2)
    return L

arr = [float(i) for i in xrange(30,51)]
d = length(arr)
l = len(arr)
for i in xrange(2000):
    for x in xrange(l):
        for y in xrange(x+1,l):
            swap(arr,x,y)
            k = length(arr)
            if(k < d):
                d = k
            else:
                swap(arr,x,y)

print d

