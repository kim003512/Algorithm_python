from collections import deque
import sys
sys.stdin=open("input.txt", "r")
sys.setrecursionlimit(10000)

dx = [-1, 1 , 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y) : # 재귀 사용
    for i in range(4) :
        
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m) :
            if arr[nx][ny] == 1 :
                arr[nx][ny] = 0
                dfs(nx, ny)

def bfs() : # queue로 풀기

t = int(input())

for _ in range(t) :
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]

    for _ in range(k) :
        x, y = map(int, input().split())
        arr[y][x] = 1

    result = 0

    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 1 :
                dfs(i, j)
                result += 1
                
    print(result)
