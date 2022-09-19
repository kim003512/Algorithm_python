from collections import deque
import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
    """ arr[x][y] = arr[y][x] = 1 """

def dfs(v) : #재귀 함수 사용
    visited[v] = True
    for i in arr[v] :
        if not visited[i]:
            dfs(i)
    """ for i in range(1, n+1) :
        if not visited[i] and arr[v][i] == 1 and arr[i][v] == 1:
            dfs(i)
            return True """
def bfs(v) :
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue :
        nx = queue.popleft()

        for i in arr[nx] :
            if not visited[i] :
                visited[i] = True
                queue.append(i)

cnt = 0

for i in range(1, n+1) :
    if not visited[i] :
        #dfs(i)
        bfs(i)
        cnt += 1

    """ if dfs(i) :
        cnt += 1 """

print(cnt)