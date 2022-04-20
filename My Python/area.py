input_min = int(input('분을 입력해주세요:'))

hour = input_min // 60
minute = input_min % 60

day = hour // 24
hour = hour % 24

print( '{}일 {}시간 {}분'.format(day,hour,minute))
