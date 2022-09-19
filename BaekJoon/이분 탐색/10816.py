#시간초과!!!!!!!!!

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
n_arr.sort()

def binarySearch(target) :
    start = 0
    end = n -1

    while start <= end :
        mid = (start + end) // 2

        if n_arr[mid] == target :
            return n_arr.count(target)
        elif n_arr[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
    return None

for i in m_arr :
    result = binarySearch(i)
    if result is None :
        print(0, end=' ')
    else :
        print(result, end=' ')