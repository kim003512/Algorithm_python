#값 입력
n, k = map(int, input().split())
#coin_list = list()
#for i in range(n):
#  coin_list.append(int(input()))
coin_list=[int(input()) for _ in range(n)]

#코인 총 개수 입력 변수
count = 0

#큰 값을 가진 것부터 나누어 구하기 위해
coin_list.sort(reverse=True)

for i in coin_list:
  if k == 0: break #남은 돈이 없을 경우 break
  count +=k//i
  k%=i

print(count)