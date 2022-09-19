#numArr = [int(input()) for _ in range(3)]

#multi =str(numArr[0] * numArr[1] * numArr[1]) 

multi = int(input()) * int(input()) * int(input())

for i in range(10) :
    print(str(multi).count(str(i)))