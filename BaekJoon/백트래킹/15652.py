N, M = map(int, input().split())
arr = []

def back(start) :
    if len(arr) == M :
        print(' '.join(map(str, arr)))
        return

    for i in range(start, N+1) :
        arr.append(i)
        back(i)
        arr.pop()

back(1)