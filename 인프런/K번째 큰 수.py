from itertools import permutations, combinations

n, K = map(int, input().split())

array = list(map(int, input().split()))
'''
sumArray = []


for i in range(0, len(array)) :
    for j in range(i+1, len(array)) :
        for k in range(j+1, len(array)) :
            sumArray.append(array[i] + array[j] + array[k])
'''

'''
for three in permutations(array, 3) :
    sumArray.append(sum(three))

setArray = set(sumArray)
setList = list(setArray)
setList.sort(reverse=True)
print(setList[K-1])
'''
sumSet = set()

for i in range(n) :
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            sumSet.add(array[i] + array[j] + array[k])

sumSet = list(sumSet)
sumSet.sort(reverse=True)

print(sumSet[K-1])
