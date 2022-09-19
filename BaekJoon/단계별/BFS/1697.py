from collections import deque

n, m = map(int, input().split())
max = 10 ** 5
dist = [0] * (max+1)

def bfs() :
    queue = deque()
    queue.append(n)

    while queue :
        x = queue.popleft()

        if x == m :
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2) :
            if 0 <= nx <= max and not dist[nx] :
                dist[nx] = dist[nx] + 1
                queue.append(nx)

bfs()
""" list = [i for i in range(100000)]

count = 0
def bfs(x, y) :
    global count
    while x != y :
        if  y-(x * 2) < y-(x-1) or y-(x+1) :
            x = x * 2
            count += 1
        else :
            if y-(x-1) < y-(x+1) :
                x = x-1
            else :
                x = x+1
            count += 1

bfs(n, m)
print(count) """