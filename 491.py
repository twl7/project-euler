from misc import *

start = time.time()
x = range(10)

total = 0
arr = [0] * 10
factorial = [1]

for i in xrange(1,11):
    factorial.append(i * factorial[-1])
    
def rec(index):
    global total
    global arr
    if(index < 10):
        if(sum(arr[:index]) < 9):
            arr[index] = 2
            rec(index+1)
        if(sum(arr[:index]) < 10):
            arr[index] = 1
            rec(index+1)
        arr[index] = 0
        rec(index+1)
    else:
        if(sum(arr) == 10):
            if(sum([i*arr[i] for i in xrange(10)]) % 11 == 1):
                arr2 = [2-c for c in arr]
                count = factorial[10]
                for i in xrange(arr[0]):
                    count *= (9-i)
                count *= factorial[10-arr[0]]
                for i in arr:
                    count /= factorial[i]
                for i in arr2:
                    count /= factorial[i]
                total += count
                
                
    
rec(0)
print total
print "Took " + str(time.time() - start)
