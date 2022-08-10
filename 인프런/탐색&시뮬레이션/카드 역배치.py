position = [list(map(int, input().split())) for _ in range(10)]

card = list(range(1, 21))

for i in range(len(position)) :
    reversedList = reversed(card[position[i][0]-1 : position[i][1]])
    card[position[i][0]-1 : position[i][1]] = reversedList

print(*card)