# 연결 요소 찾기 (connective component 찾기) 문제

""" DFS
1. 특정한 지점의 주변 상,하,좌,우를 살펴본 뒤에 주변 지점 중에서 값이 '0'이면서 
    아직 방문하지 않은 지점이 있다면 해당 지점을 방문
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면,
    연결된 모든 지점을 방문할 수 있다
3. 모든 노드에 대해 1~2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트 """

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

def dfs(x, y) :
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or y <= -1 or x >= n or y >= m :
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
        graph[x][y] = 1
        #상, 하, 좌, 우
        dfs(x-1, y) #상
        dfs(x+1, y) #하
        dfs(x, y-1) #좌
        dfs(x, y+1) #우        
        return True
    return False

result = 0
#모든 위치(노드)에 대해 음료수 채우기
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            print(i, j)
            result += 1

print(result)