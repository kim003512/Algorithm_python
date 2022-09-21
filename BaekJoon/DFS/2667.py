from collections import deque
import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
""" num = []

def dfs(x, y) : # 재귀
    if x < 0 or x >= n or y < 0 or y >= n :
        return False
    
    if arr[x][y] == 1 :
        global cnt
        cnt += 1
        arr[x][y] = 0
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True
    return False """

def bfs(x, y) : # 큐
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0
    cnt = 1

    while queue :
        x, y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < n) and (0 <= ny < n) :
                if arr[nx][ny] == 1 :
                    queue.append((nx, ny))
                    arr[nx][ny] = 0
                    cnt += 1
    return cnt

""" cnt, result = 0, 0

for i in range(n) :
    for j in range(n) :
        if dfs(i, j) == True :
            num.append(cnt)
            result += 1
            cnt = 0

print(result)
num.sort()
for i in range(len(num)) :
    print(num[i]) """

count = sorted([bfs(x, y) for x in range(n) for y in range(n) if arr[x][y] == 1])
print(len(count))
for i in range(len(count)) :
    print(count[i])
