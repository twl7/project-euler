from misc import *

mod = 500500507
heap = prime_array(10**7)
t = 1
def heapify(heap): # from head
    i = 0
    L = len(heap)
    while(i < L):
        left,right = 2*i+1,2*i+2
        if(left >= L):
            break
        if(right < L):
            if(heap[i] <= min(heap[left],heap[right])): break
            if(heap[left] < heap[right]):
                heap[i],heap[left] = heap[left],heap[i]
                i = left
            else:
                heap[i],heap[right] = heap[right],heap[i]
                i = right
        else:
            if(heap[i] < heap[left]):
                break
            else:
                heap[i],heap[left] = heap[left],heap[i]
                i = left
for i in xrange(500500):
    t *= heap[0]
    t %= mod
    heap[0] *= heap[0]
    heapify(heap)
print t
