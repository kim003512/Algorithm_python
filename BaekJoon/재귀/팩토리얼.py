# 반복문으로 구현한 n!
def factorial_iteration(n) :
    result = 1

    for i in range(1, n) :
        result *= i
    return

# 재귀 함수로 구현한 n!
def factorial_recursive(n) :
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

