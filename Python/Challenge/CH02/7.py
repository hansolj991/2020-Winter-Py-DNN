#다음에서 설명하는 함수 float.fromhex(str)를 이해하고 두 16진수 실수를 입력받아 사칙연산을 수행하는 프로그램을 작성하시오.
fir = input('첫 번째 16진수 실수 입력 >>')
sec = input('두 번째 16진수 실수 입력 >>')

flo1 = float.fromhex(fir)
flo2 = float.fromhex(sec)
acu1 = flo1 + flo2
acu2 = flo1 - flo2
acu3 = flo1 * flo2
acu4 = flo1 / flo2

print('실수1:', flo1, '실수2:', flo2)
print('합:', acu1, '\n', '차:', acu2, '\n', '곱하기:', acu3, '\n', '나누기:', acu4, '\n',)
