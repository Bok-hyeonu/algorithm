# 6064. 카잉 달력

# 1. 최소공배수까지 탐색한다.
# 2. 한 반복에 M씩 크기를 늘려 최대 반복횟수는 N(최대, 40000)

import math

# 입력 받기
T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    # 최소공배수 계산
    gcd = math.gcd(M, N)    # 최대공약수를 구하고
    lcm = M * N // gcd      # 최소공배수를 구함
    
    found = 0               # 탐색 여부 변수
    while x <= lcm:         # 최소공배수가 되기 전까지(끝 해에 도달하기 전까지)
        if (x - 1) % N + 1 == y: # 식이 맞으면
            print(x)        # 출력
            found = 1  
            break
        x += M              # 좌측값을 기준으로 더해줌
    
    if not found:           # 찾지 못한 경우 -1
        print(-1)