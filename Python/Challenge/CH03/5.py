# 5 문자열의 split() 메소드를 이용해 '14:21:45'와 같은 시각 정보를 표준으로 입력받아 입력된 문자열을 출력하고 다시 시, 분, 초로 출력하는 프로그램을 작성하시오.

time = input('시각 정보(16:30:15) 입력 >>')
hours, mins, secs = time.split(':')
print('입력 시각 정보: %s' % time)
print('{}시 {}분 {}초'.format(hours, mins, secs))