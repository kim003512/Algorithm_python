selfNumSet = set()

def selfNum(num) :
    num = num + sum(map(int, str(num)))
    return num

for i in range(1, 10001) :
    selfNumSet.add(selfNum(i))

for j in range(1, 10001) :
    if j not in selfNumSet :
        print(j)
        