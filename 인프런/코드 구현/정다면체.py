N, M = map(int, input().split())

nList = list(range(1, N+1))
mList = list(range(1, M+1))

cnt = [0] * (N+M+1)

for i in range(N) :
    for j in range(M) :
        cnt[nList[i] + mList[j]] += 1

for i in range(len(cnt)) :
    if cnt[i] == max(cnt) :
        print(i, end=' ')
'''
for i in range(N) :
    line = []
    for j in range(M) :
        line.append(nList[i] + mList[j])
    sumList.append(line)
'''

