n = int(input())
#nList = [int(input().split()) for _ in range(n)]
nList = list(map(int, input().split()))

m = int(input())
#mList = [int(input().split()) for _ in range(m)]
mList = list(map(int, input().split()))

print(sorted(nList + mList))