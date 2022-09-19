n = int(input())
#arr = [int(input().split()) for _ in range(n)]
arr = list(map(int, input().split()))

max, min = arr[0], arr[0]

for i in arr[1 : ] :
    if i > max :
        max = i
    elif i < min :
        min = i

print(min, max)

#print(min(arr), max(arr))

#AttributeError: 'map' object has no attribute 'sort'
#python3에서 map은 list를 반환하지 않고 iterator를 반환 -> sort는 list 객체의 속성이다
#따라서, list로 감싸서 list 객체로 만들어주어야 한다