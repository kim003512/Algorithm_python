N, M = map(int, input().split())
arr = []

def back(start) :
    if len(arr) == M :
        print(' '.join(map(str, arr)))
    for i in range(start, N+1) :
        if i not in arr :
            arr.append(i)
            back(i+1)
            arr.pop()

back(1)