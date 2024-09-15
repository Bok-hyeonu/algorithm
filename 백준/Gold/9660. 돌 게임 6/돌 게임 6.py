# CY가 이김 2, 7, 9, 14, 16, 21, 23, 28, 30
n = int(input())

# 게임이론
if n % 7 == 0 or n % 7 == 2:
    print('CY')
else:
    print('SK')