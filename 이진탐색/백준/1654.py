# ##랜선 자르기

# from sys import stdin

# k, n = map(int, stdin.readline().split())

# #가지고 있는 선들
# lanwire = []

# for i in range(k):
#     lanwire.append(int(stdin.readline()))


# #이분 탐색
# left = 1 #랜선의 최소 길이
# right = max(lanwire) #랜선 최대 길이

# while left <= right:
#     mid = (left + right) // 2

#     count = 0 #mid 길이씩 잘랐을 때 얻을 수 있는 랜선의 수

#     for wire in lanwire:
#         count += wire/mid
    
#     if count >= n: #랜선 수 >= 필요 수 : 자르는 단위 증가
#         left = mid + 1
    
#     elif count < n : #랜선 수 < 필요 수 : 자르는 단위 증가
#         right = mid - 1

# print(right)

from sys import stdin
K, N = map(int,stdin.readline().split())
#li = list(map(int,stdin.readlines()))
li = []

for i in range(K):
    li.append(int(stdin.readline()))
h, l = sum(li)//N, 1
# h, l = max(li), 1
while l <= h :
    mid = (h+l)//2
    cnt = sum([x//mid for x in li])
    if cnt < N:
        h = mid - 1
    elif cnt >= N:
        l = mid + 1
        ans = mid
print(ans)