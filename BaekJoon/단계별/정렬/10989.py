import sys

#수들을 직접 저장하지 않는 다른 방법 강구 -> 주어지는 수들의 개수를 카운트
n = int(sys.stdin.readline())
count = [0] * 10001 #10000 보다 작거나 같은 자연수

for _ in range(n) :
    count[int(sys.stdin.readline())] += 1

for num in range(1, 10001) :
    if count[num] != 0 :
        for j in range(count[num]) : #range()
            print(num)

'''
# 아래 방법과 같이 하면 메모리 초과 발생
n = int(sys.stdin.readline())
numList = [int(sys.stdin.readline()) for _ in range(n)]

numList.sort()

for i in numList :
    print(i)
 '''   