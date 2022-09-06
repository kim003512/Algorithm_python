import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)
total = 0

while start <= end :
    mid = (start + end) // 2
    
    for i in tree :
        if i >= mid :
            total += i - mid

    if total > M :
        start = mid + 1
    else :
        end = mid - 1

print(end)