n = int(input())

def hanoi(n, start, sub, end) :
    if n == 1 :
        print(start, end)
        return
    else :
        hanoi(n-1, start, end, sub)
        print(start, end)
        hanoi(n-1, sub, start, end)

count = 0

for _ in range(n) :
    count = 2 * count + 1

print(count)

hanoi(n, 1, 2, 3)