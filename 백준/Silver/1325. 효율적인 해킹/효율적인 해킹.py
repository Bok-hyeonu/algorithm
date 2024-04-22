# 1325 효율적으로 해킹하기

# 1. BFS 이용
# 2. 모든 노드를 시작점으로 하여 신뢰하는 컴퓨터의 수를 하나씩 증가시킴
# 3. 직접적으로 연결되지 않았더라도 BFS 탐색을 통해 신뢰하는 컴퓨터 수가 증가

import sys
from collections import deque
input = sys.stdin.readline
def BFS(v):
    cnt = 0     # 신뢰할 컴퓨터의 수
    q = deque()
    q.append(v)
    visited[v] = True
    # 큐가 비지 않을 똥안
    while q:
        # 현재 큐를 순회
        now = q.popleft()
        # 신뢰하는 컴퓨터이고
        for t in trust_relation[now]:
            # 방문하지 않은 컴퓨터라면
            if not visited[t]:
                visited[t] = True   # 방문
                cnt += 1        # 신뢰 컴퓨터 수 증가
                q.append(t)     # 다음 방문할 컴퓨터 큐에 추가
                
    return cnt
    
N, M = map(int, input().split())
trust_relation = [[] for _ in range(N+1)]       # 신뢰관계
# 입력 및 신뢰 관계 형성
for _ in range(M):
    trust, trusted = map(int, input().split())
    trust_relation[trusted].append(trust)

max_cnt = 0 # 최대 신뢰 컴퓨터의 수
most = []   # 신뢰 컴퓨터의 수가 가장 많은 배열
# 모든 노드에서 점검
for i in range(1, N+1):
    visited = [False]*(N+1) # 방문 여부 초기화
    cnt = BFS(i)
    # 최대 신뢰 컴퓨터의 수보다 큰 경우 초기화
    if max_cnt < cnt:
        max_cnt = cnt
        most = [i]
    # 같은 경우 가장 많은 배열에 추가
    elif max_cnt == cnt:
        most.append(i)

print(*most)
