import sys
import heapq

N = int(input())
heap = []

for i in range(N) :
    x = int(sys.stdin.readline())

    if x :
        heapq.heappush(heap, (-x, x))
    else :
        if len(heap) >= 1 :
            print(heapq.heappop(heap)[1])
        else :
            print(0)

