#다음 조건을 참고해 섭씨 온도를 입력받아 화씨 온도로 변환하는 프로그램을 작성하시오.
celsius = int(input('온도 입력 >>'))

acu1 = celsius * (9/5) + 32
acu2 = celsius * 2 + 30

dif = acu2 - acu1

print('정확계산: 섭씨:', celsius, ', 화씨:', acu1)
print('정확계산: 섭씨:', celsius, ', 화씨:', acu2)
print('차이:', dif).