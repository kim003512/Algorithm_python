K = int(input())

numArr = []

for _ in range(K) :
    num = int(input())

    if num == 0 :
        numArr.pop()
    else :
        numArr.append(num)

print(sum(numArr))