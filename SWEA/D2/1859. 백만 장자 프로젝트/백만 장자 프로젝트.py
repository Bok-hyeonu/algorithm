T = int(input())

for tc in range(1,T+1):
    N = int(input()) # N일 간의 미래
    prices = list(map(int, input().split())) # N일 간의 가격들
    result = 0 # 가격합
    while len(prices) != 0: # 모든 가격들에 대해
        max_pr = max(prices) # 최댓값
        idx = prices.index(max_pr) # 최댓값이 며칠 째인지

        bef = prices[:idx] # 최댓값 이전의 날 들
        prices = prices[idx + 1:] # 이후의 날들

        for i in range(len(bef)): # 최댓값 이전의 날들에 대해
            result += max_pr - bef[i] # 차이만큼 더함
    print(f"#{tc} {result}") # 출력
