'''
N, M = map(int, input().split())

arr = [[j for j in range(1, N+1)] for _ in range(M)]

for i in arr :
    print(i)
'''

N, M = map(int, input().split())
ans = []

def back() :
    if len(ans) == M :
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N+1) :
        if i not in ans :
            ans.append(i)
            back() #재귀
            ans.pop()

back()
