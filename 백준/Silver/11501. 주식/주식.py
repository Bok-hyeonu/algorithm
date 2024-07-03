# 11501. 주식

# 1. 미래를 알고 있으므로 가장 미래부터 시작해 순회
# 2. 현 시점 주가 대비 미래 최대 주가와 차익을 계산
# 3. 현 시점이 더 높으면 최대 주가 갱신. 낮으면 차익 더하기

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    revenue = 0             # 총 이익
    max_price = prices[-1]  # 현 시점 이후 최대 주가(초깃값 마감일)
    for i in range(N-2, -1, -1):    # 뒤에서부터 순회하며
        if prices[i] < max_price:   # 최대 주가보다 현 시점 주가가 낮은 경우
            revenue += max_price - prices[i]    # 해당하는만큼 차익 얻음
        else:                       # 최대 주가보다 현 시점 주가가 크면
            max_price = prices[i]   # 최대 주가 갱신
    print(revenue)  # 총 이익 출력