""" BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일
    따라서, (1, 1) 지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있다
"""

from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue : # 큐가 빌 때까지 반복하기
        x, y = queue.popleft()
        #현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= n or ny >= m :
                continue
            if graph[nx][ny] == 0 :
                continue
            if  graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0,0))