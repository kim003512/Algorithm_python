N, M = map(int, input().split())
n_arr = list(map(int, input().split()))

n_arr.sort()

start = 0
end = N - 1

while start <= end :
    mid = (start + end) // 2
    if n_arr[mid] == M :
        #print(n_arr.index(M) + 1)
        print(mid+1)
        break
    elif n_arr[mid] < M :
        start = mid + 1
    else :
        start = mid -1
