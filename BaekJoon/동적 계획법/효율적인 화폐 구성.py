n, m = map(int, input().split())

#n개의 화폐 단위 정보 입력받기
arr = []
for i in range(n) :
    arr.append(int(input()))

d = [10001] * (m + 1)

#DP 진행(Bottom-Up)
d[0] = 0

for i in range(n) : # i = 각각의 화폐 단위 의미
    for j in range(arr[i], m+1) : # j = 각각의 금액을 의미
        if d[j- arr[j]] != 10001 :
            d[j] = min(d[j], d[j-arr[i]]+1)

if d[m] == 10001 :
    print(-1)
else :
    print(d[m])
