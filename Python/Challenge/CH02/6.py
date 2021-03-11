#두 정수를 입력받은 후 산술 연산 /, %, //, ** 4개를 수행해 결과를 출력하는 프로그램을 작성하시오.
num1 = int(input('Enter First Number:'))
num2 = int(input('Enter Second Number:'))

acu1 = num1 / 5
acu2 =  num1 % num2
acu3 =  num1 // num2
acu4 =  num1 ** num2

print(num1, '/', num2, '==>', acu1)
print(num1, '%', num2, '==>', acu2)
print(num1, '//', num2, '==>', acu3)
print(num1, '**', num2, '==>', acu4)
