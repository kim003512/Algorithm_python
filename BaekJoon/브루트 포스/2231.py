n = int(input())

result = 0

for i in range(1, n+1) :
    position = list(map(int, str(i)))
    addAll = i + sum(position)

    if addAll == n : 
        result = i
        break

print(result)