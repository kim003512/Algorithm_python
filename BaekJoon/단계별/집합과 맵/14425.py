N, M = map(int, input().split())

S = set(input() for _ in range(N))
checkString = list(input() for _ in range(M))

count = 0

for i in range(M) :
    if checkString[i] in S :
        count += 1

print(count)