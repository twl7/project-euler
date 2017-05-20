f = open("matrix_sum.txt","r")
line = f.readline()
arr = []
while(line != ''):
    arr.append([int(x) for x in line.split()])
    line = f.readline()
N = len(arr)
values = range(N-1,-1,-1)
for iteration in xrange(N**3):
    for i in xrange(N-1):
        for j in xrange(i+1,N):
            if(arr[i][values[j]] + arr[j][values[i]] >= arr[i][values[i]] + arr[j][values[j]]):
                values[i], values[j] = values[j],values[i]
print sum([arr[i][values[i]] for i in xrange(N)])

f.close()
