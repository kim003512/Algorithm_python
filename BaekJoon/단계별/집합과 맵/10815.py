import sys

N = int(sys.stdin.readline())
#sanCardList = [map(int, sys.stdin.readline().split()) for _ in range(N)]
sanCardList = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
#cardList = [map(int, sys.stdin.readline().split()) for _ in range(M)]
cardList = list(map(int, sys.stdin.readline().split()))

#이진탐색
sanCardList.sort() #이분탐색은 정렬된 리스트에서만 가능

def binarySearch(num) :
    start = 0
    end = N -1

    while start <= end :
        mid = (start + end) // 2

        if sanCardList[mid] == num :
            return 1
        elif sanCardList[mid] > num :
            end = mid -1
        else :
            end = mid + 1
    return 0

for i in cardList :
    print(binarySearch(i), end=' ')

#딕셔너리
cardDic = {cardList[i] : 0 for i in range(len(cardList))}

for i in range(N) :
    if sanCardList[i] in cardDic.keys() :
        cardDic[sanCardList[i]] += 1

print(" ".join(map(str, list(cardDic.values()))))
    
#set
input()
A = set(map(int, input().split()))
input()
B = list(map(int, input().split()))

for i in B :
    if i in A :
        print(1, end=' ')
    else :
        print(0, end=' ')

#주어지는 입력 값이 엄청 크기 때문에 if in 문법을 통해서 찾는다면 무조건 시간 초과가 날 것이다.
#그럼으로 알고리즘 분류가 이분 탐색으로 되있다는게 힌트

# 시간 초과
existCheckList = [0] * M

for i in range(len(sanCardList)) :
    if sanCardList[i] in cardList :
        existCheckList[cardList.index(sanCardList[i])] = 1

for i in range(len(existCheckList)) :
    print(existCheckList[i])

