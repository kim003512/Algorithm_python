n = int(input())

arr = list(map(int, input().split()))

maxNum = max(sorted(arr))

print(max(sorted(arr)) * min(sorted(arr)))