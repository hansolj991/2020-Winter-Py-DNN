#네 자릿수 정수를 입력받은 후 그 정수를 역순으로 출력하는 프로그램을 작성하시오.
data = int(input('네 자릿수 정수 입력>>'))

print( int(str(data)[::-1]))