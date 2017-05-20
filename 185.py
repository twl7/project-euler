
f = open("numbermind.txt","r")

arr = []
line = f.readline()
while(not line == ''):
    arr.append([int(x) for x in line.split()])
    line = f.readline()
for m in arr:
    m[0] = str(m[0])
numbers = [x[0] for x in arr]
L = len(numbers)
counts = [x[1] for x in arr]
N = len(numbers[0])

def numbermind(number, digit, counts):
    index = len(number)
    s = str(digit)
    
    for i in xrange(L):
        if(numbers[i][index] == s):
            if(counts[i] >= 1):
                counts[i] -= 1
            else:
               return
    new = number + s + ""
    
    if(index == N-1):
        if(sum(counts) == 0):
            print new
        
    else:
        for i in xrange(10):
            numbermind(new,i,counts + [])
for i in xrange(0,10):
    numbermind("",i,counts+[])
           
               


f.close()
