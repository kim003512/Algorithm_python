num = int(input())

for i in range(num) :
    N, s, e, k = map(int, input().split())

    #numList = list(int(input().split()) for _ in range(N))

    numList = list(map(int, input().split()))
    numList = numList[s-1 : e]

    numList.sort()

    print("#%d %d" %(i+1, numList[k-1]))