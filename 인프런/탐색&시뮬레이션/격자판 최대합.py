n = int(input())

arr = [[0 for j in range(5)] for i in range(5)]

for i in range(n) :
    arr[i] = list(map(int, input().split()))

sumArray = []
for i in range(n) :
    sumArray.append(sum(arr[i]))
    sumArray.append(sum(arr[i][0]))
    # for j in range(n) :
    #     sumArray.append(sum(arr[i][j]))

print(sumArray)