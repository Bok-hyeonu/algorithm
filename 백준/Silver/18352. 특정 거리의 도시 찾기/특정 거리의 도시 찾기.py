# 18352. 특정 거리의 도시 찾기
import sys
# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
# 도시 정보 입력
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
# 최단 거리 배열
distance = [0]*(N+1)
# 방문 여부 배열
visited = [0]*(N+1)
# BFS 탐색
def BFS(start):
    q = [start]
    visited[start] = 1
    while q:
        new_q = []
        for now in q:
            # 인접 도시 중에서
            for next in graph[now]:
                # 방문한 도시는 배제
                if visited[next]:
                    continue
                # 방문 표시
                visited[next] = 1
                # 최단거리 갱신
                distance[next] = distance[now] + 1
                # 다음 도시 추가
                new_q.append(next)
        q = new_q
BFS(X)
is_result = 0
for i in range(1, N+1):
    if distance[i] == K:
        is_result = 1
        sys.stdout.write(f'{i}\n')
if is_result==0:
    sys.stdout.write('-1\n')