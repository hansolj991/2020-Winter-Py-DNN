# 다음 조건을 참고해 지구를 원이라고 보고 원의 둘레를 계산해 실제와의 차이를 알아보는 프로그램을 작성하시오.
same = 2 * 3.141592 * 6378.1
length = 40120

result = same - length

print('알려진 지구 둘레:', length)
print('지구와 같은 원둘레:', same)
print('차이:', result, '(km)')
