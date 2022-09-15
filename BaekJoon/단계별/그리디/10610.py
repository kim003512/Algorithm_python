#어떠한 수 k가 30의 배수가 되기 위해서는 k가 10과 3의 배수여야 함
#즉, k의 모든 자리 수의 합이 3의 배수이며, k의 마지막 자리는 0이어야 함
#따라서, 숫자 n을 입력받은 후 각 자리의 수가 3의 배수이며 0을 포함하는지 확인

# 그리디 알골리즘이 적용되는 부분은 가장 큰 수를 만들때 가장 큰 값이 들어가기 때문

""" n = input()
arr = [i for i in n]
arr.sort(reverse=True)

if int(''.join(arr)) % 30 == 0 :
    print(''.join(arr))
else :
    print(-1) """

k = input()
k = [int(i) for i in k]

if (sum(k) % 3) == 0 and 0 in k :
    print(''.join(map(str, sorted(k, reverse=True))))
else :
    print(-1)