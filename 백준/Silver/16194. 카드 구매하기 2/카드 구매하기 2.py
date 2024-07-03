# 16194. 카드 구매하기 2

# 1. i+1개 들이 카드팩들을 순회하며 카드를 j개 산 경우의 최저가를 갱신해간다
# 2. 카드 N개를 산 경우 최저가를 출력한다.

N = int(input())                            # 민규가 구매하려고 하는 카드의 수
prices = list(map(int, input().split()))    # 카드팩의 가격

DP = [0]
DP += prices            # 기존의 가격을 저장
for i in range(N):      # i+1개 들이 카드팩을 순회하며
    price = prices[i]   # 해당 팩 가격 설정
    for j in range(i+1, N+1): # 카드를 i+1개 산 경우부터 확인 가능
        # 기존 최저가와 j - (i+1)개 가격에서 i + 1개 들이 카드팩을 산 경우를 비교해 최저가 갱신
        DP[j] = min(DP[j-i-1]+price, DP[j])

print(DP[N])