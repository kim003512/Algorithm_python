n = int(input())
personList = [list(map(int, input().split())) for _ in range(n)]

for i in range(len(personList)) :
    rank = 1
    for j in range(len(personList)) :
        if personList[i][0] < personList[j][0] and personList[i][1] < personList[j][1] :
            rank += 1
    print(rank, end=" ")
            
'''
첫번째 꺼는 i

if(A1 < B1) and (A2 < B2) :
    i = 두번째 꺼 and i = i+1
else :
    두번째 꺼 = i

'''
