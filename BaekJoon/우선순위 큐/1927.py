import sys
import heapq as hp

N = int(input())
heap = []

for i in range(N) :
    x = int(sys.stdin.readline())

    if x : 
        hp.heappush(heap, (x, x))
    else :
        if len(heap) >= 1 :
            print(hp.heappop(heap)[0])
        else :
            print(0)