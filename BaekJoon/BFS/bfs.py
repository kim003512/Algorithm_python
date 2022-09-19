from collections import deque

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False] * 9

def bfs(graph, start, visited) :
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True

    #큐가 빌 때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아와 출력
        v = queue.popleft()
        print(v, end =' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i) 
                visited[i] = True

bfs(graph, 1, visited)
