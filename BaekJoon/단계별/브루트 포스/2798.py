N, M = map(int, input().split(' '))
cards = list(map(int, input().split(' '))) #M만큼의 수가 들어오는지 확인?

result = 0

for i in range(0, len(cards)) :
    for j in range(i+1, len(cards)) :
        for k in range(j+1, len(cards)) :
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M :
                result = max(result, sum)

print(result)
                
