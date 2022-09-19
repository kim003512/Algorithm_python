# 각 노드가 연결된 정보를 표현 (2차원 리스트)
# 보통 1번부터 시작하므로 0번 인덱스는 비워져 있음
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문한 정보를 저장 (1차원 리스트)
#1~8번 노드까지 가지고 있기 때문에 인덱스 0은 사용하지 않기 위해 하나 더 큰 크기로 1차원 리스트 초기화
visited = [False] * 9 

def dfs(graph, v, visited) :
    visited[v] = True # 현재 노드 방문 처리
    print(v, end = ' ')

    for i in graph[v] :
        if not visited[i] :
            dfs(graph, i, visited) 

dfs(graph, 1, visited)