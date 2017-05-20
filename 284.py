from misc import *
start= time.time()
n = 10000
t = 1
chars = [str(i) for i in xrange(10)] + ['a','b','c','d']
def to_14(num):
    ans = ""
    while(num > 0):
        ans = chars[num % 14] + ans
        num /= 14
    return ans
val = [7,8]
for s in val:
    d = s
    t += d
    for i in xrange(1,n):
        m = 14**i
        k = 14*m
        for digit in xrange(14):
            if(s*s % k == s):
                d += digit
                if(digit > 0):
                    t += d
                break
            
            s += m
        
print to_14(t)
print time.time() - start
