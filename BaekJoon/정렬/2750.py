n = int(input())
numList = [int(input()) for _ in range(n)]

# numList.sort()

#버블 정렬
for i in range(len(numList)) :
    for j in range(len(numList)) :
        if numList[i] < numList[j] :
             numList[i], numList[j] = numList[j], numList[i]

#삽입정렬
for i in range(1, len(numList)) :
    while((i >= 0) and numList[i] < numList[i-1]) :
        numList[i], numList[i-1] = numList[i-1], numList[i]
        i -= 1

for i in numList :
    print(i)