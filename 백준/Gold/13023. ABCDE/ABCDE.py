# 13023. ABCDE

# 목표 : 깊이가 5인 경우를 찾는다
# 1. 친구 관계(간선)가 주어지면 각 친구(노드)들을 양방향 연결한다.
# 2. 시작점을 조절하면서 깊이가 5가 되면 중단한다.
# 3. 최종적으로 깊이가 5이면 1, 아니면 0을 출력한다.

import sys
N, M = map(int, sys.stdin.readline().split())   # 사람 수, 관계 수
isPossible = 0          # 가능 여부를 판단하는 변수(0)
relationships = [[] for _ in range(N)]    # 관계파악을 위해 관계 배열 생성
visited = [0]*N                           # 방문 배열 생성

def DFS(now, depth):  # now : 현재 순회하는 친구, depth : 깊이
    
    global isPossible
    # 종료 조건 : 깊이 5
    if depth == 5:
        isPossible = 1
        return
    visited[now] = 1        # 방문 표시
    
    # now의 친구들을 dfs 탐색
    for fri in relationships[now]:
        # 탐색하지 않은 친구라면
        if not visited[fri]:
            # 깊이 1 증가시키고 탐색
            DFS(fri, depth + 1)
    
    visited[now] = 0        # 다른 친구 기준 탐색을 위해 0으로 수정

# 친구 상호 간 관계 설정
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    relationships[s].append(e)
    relationships[e].append(s)

# 친구 순서대로 탐색
for i in range(N):
    DFS(i, 1)
    if isPossible:
        break

print(isPossible)   # 가능 여부 출력