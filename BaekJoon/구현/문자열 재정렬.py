""" 문자열이 입력되었을 때 문자를 하나씩 확인
숫자인 경우 따로 합계를 계산
알파벳의 경우 별도의 리스트에 저장
결과적으로 리스트에 저장된 알파벳을 정렬해 출력, 합계를 뒤에 붙여 출력 """

data = input()
result = []
value = 0

#문자 하나씩 확인
for x in data :
    if x.isalpha() :
        result.append(x)
    else :
        value += int(x)

result.sort()

if value != 0 :
    result.append(str(value))

#최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))