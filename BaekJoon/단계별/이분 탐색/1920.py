n = int(input())
numList = list(map(int, input().split()))
m = int(input())
checkNum = list(map(int, input().split()))
numList.sort()

def binarySearch(target) :
    start = 0
    end = n - 1

    while start <= end :
        mid = (start + end) // 2

        if numList[mid] == target :
            return True
        elif numList[mid] < target :
            start = mid + 1
        else :
            end = mid - 1

for i in checkNum :
    if binarySearch(i) :
        print(1)
    else :
        print(0)