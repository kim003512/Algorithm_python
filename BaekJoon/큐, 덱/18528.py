import sys
from queue import Queue
from collections import deque

N = int(sys.stdin.readline())

#que = Queue()

queue = deque()

for _ in range(N) :
    command = sys.stdin.readline().split()
    if command[0] == 'push' :
        queue.append(command[1])
    elif command[0] == 'pop' :
        '''if queue.qsize() != 0 :
            first = queue.popleft()
            print(first)
        else :
            print(-1)'''
        if not queue :
            print(-1)
        else :
            print(queue[0])
            queue.popleft()
    elif command[0] == 'size' :
        print(len(queue))
    elif command[0] == 'empty' :
        '''if que.qsize() != 0 :
            print(0)
        else :
            print(1)'''
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif command[0] == 'front' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
    elif command[0] == 'back' :
        if not queue :
            print(-1)
        else :
            print(queue[-1])