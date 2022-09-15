# https://www.acmicpc.net/problem/11000

""" 핵심 아이디어는 강의가 겹치는지 확인하는 것
강의실이 추가로 필요한 경우 = 어떤 한 강의가 끝나지 않았는데 다른 강의 시작하는 경우
이를 관리하기 위해서는 우선 순위 큐를 활용
    우선순위 큐 = 큐의 형태를 가지고 있지만 안의 노드들이 정렬되어 있는 큐
    우선순위 큐를 사용하면 끝나는 시간이 가장 빠른 강의부터 pop 가능

1. 강의 리스트 정렬
2. 첫번째 강의가 끝나는 시간을 우선순위 큐에 추가
3. 강의 리스트의 1번째 인덱스부터 마지막까지 반복문을 실행
    1. 우선순위 큐에 첫번째 인덱스에 접근 (항상 끝나는 시간이 가장 빠른 순)
    2. 만약 강의의 시작 시간이 우선순위 큐의 첫번째 인덱스보다 작다면
     해당 강의의 끝나는 시간을 우선순위 큐에 추가
    3. 아니라면 우선순위 큐의 첫번째 인덱스를 pop한 후 
    해당 강의의 끝나는 시간을 우선순위 큐에 추가

위의 과정을 전부 거치면 우선순위 큐의 크기 = 필요한 강의실 개수    
"""
import heapq

n = int(input())

lessons = [list(map(int, input().split())) for _ in range(n)]
lessons.sort()

lessons_queue = []
heapq.heappush(lessons_queue, lessons[0][1]) #첫번째 강의가 끝나는 시간을 우선순위 큐에 추가
print('첫번째 queue', lessons_queue)

for i in range(1, n) :
    if lessons[i][0] < lessons_queue[0] :
        heapq.heappush(lessons_queue, lessons[i][1]) 
        print('두번째 queue', lessons_queue)

    else :
        heapq.heappop(lessons_queue)
        heapq.heappush(lessons_queue, lessons[i][1])
        print('세번째 queue', lessons_queue)


print(len(lessons_queue))


# 첫뻔째 원소(수업)을 기준으로 시작한다
# 첫번째 원소의 끝나는 시간을 가지고 남은 원소들의 시작 시간과 비교해 
# [첫번째 원소 끝나는 시간 <= 남은 원소들의 시작 시간]일 경우 한 강의실로 
"""
n = int(input())
lessons = [list(map(int, input().split())) for i in range(n)]
lessons.sort(key=lambda x:x[0])

count = 0
now_lesson = lessons[0]

for lesson in lessons :
    if now_lesson[1] <= lesson[0] :
        count += 1
        del now_lesson, lesson
        now_lesson = lessons[0]
    count += 1
    del now_lesson
    now_lesson = lessons[0]

print(count)"""
