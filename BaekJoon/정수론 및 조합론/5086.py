#각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 
# 배수라면 multiple을, 둘 다 아니라면 neither를 출력

import sys

while True :
    a, b = map(int, sys.stdin.readline().split())

    if a == b == 0 :
        break

    if a % b == 0 :
        print("multiple")
    elif b % a == 0 :
        print("factor")
    else :
        print("neither")