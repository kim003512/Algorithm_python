n = int(input())
#meetings = [list(map(int, input().split())) for _ in range(n)]

meetings = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
#끝나는 시간을 기준으로 정렬해야 더 많은 회의를 고려할 수 있음
#끝나는 시간이 같다면 시작하는 시간 오름차순 정렬해야 더 많은 회의 진행 가능
#즉, 1.끝나는 시간의 오름차순, 2.시작하는 시간의 오름차순
#meetings.sort(key=lambda x: (x[1], x[0])) 

first_meeting = meetings[0]
count = 1

for i in range(1, n) :
    #첫 원소의 끝나는 시간보다 다음 회의 시간의 시작 시간이 크거나 같아야 함

    if first_meeting[1] <= meetings[i][0] :
        first_meeting = meetings[i]
        count += 1

print(count)