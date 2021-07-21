from random import *
number1 = randint(1,6)
number2 = randint(1,6)
print("주사위 던지기")
print('주사위1:' , number1)
print('주사위2:' , number2)

print('\n''실행할 연산의 종류를 입력하세요.')
print(' 1. 덧셈', '2.뺄셈', '3. 곱셉' , '4.나눗셈', '5.나머지 구하기', '연산 종류:1')
print ('덧셈 결과:', number1+number2)


print('\n''별찍기')
end=number1+number2
for i in range(1, end+1):
    print("*"*i)
