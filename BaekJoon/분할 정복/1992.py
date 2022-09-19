N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

def checkQuard(x, y, N) :
    check = arr[x][y]

    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if check != arr[i][j] :
                print("(", end='')
                checkQuard(x, y, N//2)
                checkQuard(x, y+N//2, N//2)
                checkQuard(x+N//2, y, N//2)
                checkQuard(x+N//2, y+N//2, N//2)
                print(")", end='')
                return

    if check == 1 :
        print(1, end='')
    else :
        print(0, end='')

checkQuard(0, 0, N)