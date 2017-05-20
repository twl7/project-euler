import time

start = time.time()
a = [[0] * 4 for i in xrange(4)]

t = 0
arr = [[2,0],[2,1],[3,0],[3,1],[3,2]]
for i in xrange(10000):
    s = 0
    for j in xrange(4):
        a[0][j] = i % 10
        s += a[0][j]
        i /= 10
    for j in xrange(100000):
        for x in arr:
            a[x[0]][x[1]] = j % 10
            j /= 10
        a[3][3] = s - a[3][0] - a[3][1] - a[3][2]
        if(a[3][3] < 0 or a[3][3] > 9):
            continue
        a[1][0] = s - a[0][0] - a[2][0] - a[3][0]
        if(a[1][0] < 0 or a[1][0] > 9):
            continue
        a[1][1] = s - a[0][1] - a[2][1] - a[3][1]
        if(a[1][1] < 0 or a[1][1] > 9):
            continue
        a[1][2] = s - a[3][0] - a[2][1] - a[0][3]
        if(a[1][2] < 0 or a[1][2] > 9):
            continue
        a[2][2] = s - a[3][3] - a[1][1] - a[0][0]
        if(a[2][2] < 0 or a[2][2] > 9):
            continue
        a[1][3] = s - a[1][0] - a[1][1] - a[1][2]
        if(a[1][3] < 0 or a[1][3] > 9):
            continue
        a[2][3] = s - a[2][0] - a[2][1] - a[2][2]
        if(a[2][3] < 0 or a[2][3] > 9):
            continue
        if(a[0][2] + a[1][2] + a[2][2] + a[3][2] != s):
            continue
        if(a[0][3] + a[1][3] + a[2][3] + a[3][3] != s):
            continue
        t+=1
print t
print time.time() - start
