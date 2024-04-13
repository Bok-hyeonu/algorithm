# 2239. 동전 1

# K원을 만드는 가짓수는 n종류의 동전을 순회하며, 
# K-동전가치의 가짓수를 더하는 것이다. 예를 들어, 1원과 2원을 가지고
# 5원을 만드는 방법은 4원에서 1원을 더하는 방법과 3원에서 2원을 더하는 
# 방법이 있다. 따라서, (5-1)원을 만드는 가짓수와 (5-2)원을 만드는 가짓수를
# 더해주면 5원을 만드는 가짓수이다. 

# 로직
# 1. 목표 가치보다 큰 가치의 동전 제거
# 2. 남은 동전들을 순회하며 동전 가치를 만드는 방법을 갱신해 나간다.

import sys

# n : 동전의 가짓수, k : 목표 가치
n , k = map(int, sys.stdin.readline().split())
# n개 동전의 가치
values = [int(sys.stdin.readline()) for _ in range(n)] 
# 목표가치보다 가치가 큰 필요없는 동전은 제거한다.
values.sort()
for i in range(n):
    if values[i] > k:
        values = values[:i]
        break

# DP
D = [0]*(k+1)   # K원까지 가짓수를 알아내기 위해 크기 K+1의 배열 생성 
D[0] = 1        # 0원을 만드는 법은 아무 것도 안 하는 경우 1가지

# 동전들을 순회하며
for coin in values:
    # 해당 동전의 가치부터 K원까지 순회
    for now in range(coin, k+1):
        # now원을 만드는 방법은 now-coin원에서 coin원을 더한다.
        D[now] += D[now-coin]

print(D[k])     # K원을 만드는 가짓수 출력