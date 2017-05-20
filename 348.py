import misc
import math

d = [""] + [str(i) for i in xrange(10)]
for i in xrange(500,100000):
    for digit in d:
        s = str(i)
        number = int(s + digit + misc.reverse(s))
        count = 0
        cube = 2
        while(cube**3 < number):
            root = math.sqrt(number -cube**3)
            if(root == int(root)):
                count += 1
            cube += 1
        if(count == 4):
            print number
