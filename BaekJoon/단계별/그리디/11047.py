# https://www.acmicpc.net/problem/11047
# 큰 동전만을 생각하고 다른 동전은 생각하지 않기 때문에 
# 매순간 최적이라고 생각되는 경우를 선택하는 탐욕 알고리즘

n, m = map(int, input().split())
coins = [int(input()) for i in range(n)]

result = 0

for coin in reversed(coins) : #받아온 동전은 오름차순 정렬이기 때문에 이를 내림차순으로
    if m >= coin : 
        result += m // coin
        m = m % coin
    
    if m <= 0 :
        break

print(result)