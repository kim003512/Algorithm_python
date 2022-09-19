import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
blue, white = 0, 0

def colorPaper(x, y, N) :
    global blue, white
    color = board[x][y]

    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != board[i][j] :
                colorPaper(x, y, N//2)
                colorPaper(x, y+N//2, N//2)
                colorPaper(x+N//2, y, N//2)
                colorPaper(x+N//2, y+N//2, N//2)
                return 
                
    if color == 0 :
        white += 1
    else :
        blue += 1

colorPaper(0, 0, N)

print(white)
print(blue)