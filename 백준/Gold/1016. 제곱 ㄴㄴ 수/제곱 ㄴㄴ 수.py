# 1016. 제곱 ㄴㄴ 

# 1. 최소부터 최대까지 제곱수의 배수를 제곱수로 체크한다.
# 2. 체크 안 된 수는 제곱 ㄴㄴ수이므로 그 가짓수를 센다.
# 3. 메모리와 탐색 시간을 줄이기 위해 check 배열의 길이를 최대 - 최소로 지정한다.

import math
Min, Max = map(int, input().split())
check = [0]*(Max - Min + 1)

# 최댓값까지의 제곱수를 구한다
for i in range(2, int(math.sqrt(Max) + 1)):
    jegob = i*i # 제곱수
    st = int(Min / jegob) # 탐색 시작점
    # 나머지가 있는 경우 1을 더해 최솟값보다 큰 제곱수에서 시작하도록 설정
    if Min % jegob != 0:
        st += 1
    for j in range(st, int(Max / jegob) + 1):
        # 제곱수로 나누어 떨어지면 true로 변경
        check[int((j * jegob) - Min)] = 1

cnt = 0
# 제곱수인지 아닌지를 셈
for i in range(Max - Min + 1):
    # 제곱이 아닌 수인 경우 + 1
    if not check[i]:
        cnt += 1

print(cnt)