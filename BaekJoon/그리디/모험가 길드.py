n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0  #현재 그룹에 포함된 모험가의 수

for i in data : #공포도를 낮은 것부터 하나씩 확인
    count += 1
    print("i = " , i)
    print("count = " , count)
    if count >= i :
        result += 1 # 총 그룹 수 증가
        count = 0 # 현재 그룹에 포함된 모함가의 수 초기화

print(result)