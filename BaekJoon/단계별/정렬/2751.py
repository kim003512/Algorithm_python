import sys

n = int(sys.stdin.readline())
numList = [int(sys.stdin.readline()) for _ in range(n)]

numList.sort()

for i in numList :
    print(i)