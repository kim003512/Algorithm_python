import sys

n = int(sys.stdin.readline())

array = list(list(map(int, input().split())) for _ in range(n))
checkArray = [[0]*7 for _ in range(1, n+1)]


for i in range(n) :
    for j in range(len(array[i])) :
        checkArray[i][array[i][j]] += 1

print(checkArray)
prize = list()

for i in range(n) :
    if 3 in checkArray[i] :
        prize.append(10000 + (checkArray[i].index(3) * 1000))
    elif 2 in checkArray[i] :
        prize.append(1000 + (checkArray[i].index(2) * 100))
    else :
        print(max([i for i in range(len(checkArray[i])) if 1 in checkArray[i]]))
        prize.append(max([i for i in range(len(checkArray[i])) if 1 in checkArray[i]]) * 100)

print(max(prize))
        
'''
3 -> 10000 + x * 1000
2 -> 1000 + x * 100
else -> (그 중 가장 큰 눈) * 100
'''