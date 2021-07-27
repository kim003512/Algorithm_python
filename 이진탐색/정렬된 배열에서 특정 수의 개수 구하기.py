# n ,m = map(int, input().split())

# for _ in n:
#     array = list(map(int, input().split()))

# count = 0

# for x in array : 
#     if(array[x] == m):
#         count +=1

# print(count)

# #특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제 해결 
# from bisect import bisect_left, bisect_right

# #값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
# def count_by_range(array, left_value, right_value):
#     right_index = bisect_right(array, right_value)
#     left_index = bisect_left(array, left_value)
#     return right_index, left_index

# n,x = map(int, input().split()) #데이터의 개수 n, 찾고자 하는 값 x 입력 받기
# array = list(map(int, input().split())) #전체 데이터 입력받기

# #값이 [x,x] 범위에 있는 데이터의 개수 계산
# count = count_by_range(array, x, x)

# #값이 x인 원소가 존재하지 않는다면
# if count == 0:
#     print(-1)
# #값이 x인 원소가 존재한다면
# else:
#     print(count)

from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
array = list(map(int, input().split()))

count = bisect_right(array, x) - bisect_left(array, x)
if count == 0:
    print(-1)
else:
    print(count)