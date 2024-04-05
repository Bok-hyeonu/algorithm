# 13305. 주유소
# 1. 각 도시의 주유소를 순회하며 최저가 기름값을 갱신한다.
# 2. 다음 도시로 이동할 때는 이동거리만큼 현재 도시까지 기름값이 최저였던 도시에서 주유한다.
# 2-1. 마지막 도시의 주유소 가격은 필요 없다.
# 3. 총 가격 합을 구한다.

N = int(input())
distances = list(map(int, input().split()))     # 주유소 간 거리
prices = list(map(int, input().split()))        # 기름 가격

prices.pop()    # 마지막 도시의 기름 가격은 필요 없다.

min_price = int(1e9)                        # 최저가
total_price = 0                             # 총 가격

for i in range(N-1):                        # 각 도시의 기름값을 순회하며
    min_price = min(min_price, prices[i])   # 기름값이 최저가인 도시에서
    total_price += min_price*distances[i]   # 다음 최저가 도시까지의 거리만큼 충전

print(total_price)