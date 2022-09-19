from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for i in range(n+1)] 

for i in range(m) :
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

# graph = [list(map(int, input().split())) for _ in range(m)]
visited = [False] * (n+1)

def dfs(v) :
    visited[v] = True
    print(v, end=' ')

    for i in range(1, n+1) :
        if not visited[i] and graph[v][i] == 1 :
            dfs(i)


def bfs(v) :
    visited[v] = True
    queue = deque()
    queue.append(v)

    while queue :
        nowV = queue.popleft()
        print(nowV, end=' ')
        for i in range(1, n+1) :
            if graph[nowV][i] == 1 and not visited[i] :
                queue.append(i)
                visited[i] = True

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)