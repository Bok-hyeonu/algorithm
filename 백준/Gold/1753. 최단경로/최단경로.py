# 1753. 최단 경로
import sys
from heapq import heappush, heappop

# 1. 우선순위 큐를 이용한 다익스트라 알고리즘을 이용
# 2. 거리가 가까운 순서대로 탐색
# 3. 단 방문한 노드인 경우(이미 한 번 탐색한 노드인 경우) 탐색 진행 X
# 4. 이미 방문 거리가 더 짧은 방법이 있다면 탐색 진행 X

def dijkstra(start):
    pq = []

    # 시작점의 거리, 노드 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 거리 초기화
    distance[start] = 0

    while pq:
        # 최단 비용 노드에 대한 정보
        dist, now = heappop(pq)
        # 방문한 노드인 경우 탐색 종료
        if visited[now]:
            continue
        visited[now] = 1
        # now에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이전에 여기까지 온 거리가 더 짧다면 탐색 진행 X
            if new_dist >= distance[next_node]:
                continue
            # 최소거리 갱신
            distance[next_node] = new_dist 
            # 다음 거리 탐색
            heappush(pq, (new_dist, next_node))

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split()) # 정점의 수, 간선의 수
K = int(sys.stdin.readline()) # 시작 정점의 번호
# 누적 비용을 저장할 변수
distance = [INF]*(V+1)
visited = [0]*(V+1)
# 인접 리스트
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v)) # 가중치, 방향 순으로 저장

# 다익스트라 알고리즘 수행
dijkstra(K)
for i in range(1, V+1):
    if distance[i] > 500000:
        sys.stdout.write('INF\n')
    else:
        sys.stdout.write(f'{distance[i]}\n')
