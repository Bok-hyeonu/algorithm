# 20303. 할로윈의 양아치

# 1. 1번 친구부터 순회하며 방문하지 않은 1번 친구 관계 모든 친구의 사탕을 뺏는다.(BFS)
# 2. 친구의 수가 K 이상이면 뺏을 수 없다.
# 3. 사탕을 빼앗긴 친구의 수가 K 이하이면 합이 K 미만이라면 다른 친구 관계의 사탕도 빼앗을 수 있다.
# 4. 다른 친구 관계도 탐색하며 사탕을 빼앗을 수 있는 최댓값을 계산한다.(DP)

import sys
from collections import deque
input = sys.stdin.readline

# 아이들의 수(노드), 친구 관계 수(간선), 최소 아이 수
N, M, K = map(int, input().split())

# 각 아이들이 가지고 있는 사탕 수
candies = [0]
candies += list(map(int, input().split()))

# 친구 관계
connects = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    connects[s].append(e)
    connects[e].append(s)

visited = [0]*(N+1) # 탐색 여부

def bfs(start): # 시작 위치
    q = deque([start])
    visited[start] = 1      # 뺏음 표시
    cnt = 1                 # 뺏은 친구의 수
    total = candies[start]  # 사탕의 수
    while q:
        now = q.popleft()       # 확인할 친구
        for t in connects[now]: # 친구들을 순회하며
            if not visited[t]:  # 뺏은 적이 없다면 뺏음
                cnt += 1
                total += candies[t]
                visited[t] = 1  # 방문 표시
                q.append(t)     # 다음에 탐색할 친구 관계

    return total, cnt

# BFS를 통해 각 컴포넌트의 사탕 수와 친구 수를 계산
components = []
for i in range(1, N + 1):
    if not visited[i]:
        candy, kids = bfs(i)
        if kids < K:
            components.append((kids, candy))

# DP를 통해 최다 사탕 수를 계산
DP = [0] * K
for kids, candy in components:
    for j in range(K - 1, kids - 1, -1):
        DP[j] = max(DP[j], DP[j - kids] + candy)
        
print(DP[K-1])    # 최다 사탕 수