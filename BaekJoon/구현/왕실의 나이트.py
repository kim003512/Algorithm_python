# 왕실의 나이트 (전형적인 시뮬레이션 , 완전 탐색 문제이면서 2차원 좌표를 이용하는 구현 문제)
# 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인
# 리스트를 이용하여 8가지 방향에 대한 방향 벡터를 정의
	
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
	
# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps :
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        result += 1

print(result)
