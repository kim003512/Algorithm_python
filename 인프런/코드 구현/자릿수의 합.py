n = int(input())

numList = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    for i in list(str(x)) :
        sum += int(i)
    return sum
    

numDic = {}
for i in range(n) :
    numDic[numList[i]] = digit_sum(numList[i])

maxValue = max(numDic, key=numDic.get)

print(maxValue)