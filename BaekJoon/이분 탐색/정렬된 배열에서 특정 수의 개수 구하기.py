from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
arr = list(map(int, input().split()))

count = bisect_right(arr, x) - bisect_left(arr, x)

if count == 0 :
    print(-1)
else :
    print(count)
'''
def binary(target) :
    start = 0
    end = len(arr) - 1
    global count

    while start <= end :
        mid = (start + end) // 2

        if arr[mid] == target :
            print(arr.count(target))
            break
            for i in range(mid, -1, -1) :
                if arr[i] == target :
                    count += 1
                else :
                    break
            
            for j in range(mid+1, len(arr)) :
                if arr[j] == target :
                    count += 1
                else :
                    break

            return count
        elif arr[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
binary(x)
if count == 0 :
    print(-1)
else :
    print(count)'''