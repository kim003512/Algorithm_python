N, M  = map(int, input().split())

#nArray = set(input() for _ in range(N))
#mArray = set(input() for _ in range(M))

nArray = set(map(int, input().split()))
mArray = set(map(int, input().split()))

print(len(nArray-mArray) + len(mArray - nArray))