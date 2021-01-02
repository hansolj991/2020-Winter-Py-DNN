distance = 384400
unit = 10000
manUnit, remainder = divmod(distance, unit)  #divmo(a,b) a와 b의 몫과 나머지 구할수 있음
print('지구에서 달까지의 거리:' , manUnit, '만', remainder,'킬로미터')
