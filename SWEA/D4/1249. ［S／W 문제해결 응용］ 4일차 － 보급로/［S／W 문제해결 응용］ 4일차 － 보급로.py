from heapq import heappush, heappop
 
def dijkstra(start):
    pq = []
 
    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    costs[start[0]][start[1]] = 0
    while pq:
        # 최단 거리 노드에 대한 정보
        cost, now = heappop(pq)
 
        # now에서 인접한 다른 노드 확인
        for to in graph[now[0]][now[1]]:
            next_cost = to[2]
            next_node = to[1]
 
            # 누적 거리 계산
            new_cost = cost + next_cost
 
            # 이미 더 짧은 거리로 간 경우 pass
            if new_cost >= costs[next_node[0]][next_node[1]]:
                continue
 
            costs[next_node[0]][next_node[1]] = new_cost # 누적 거리를 최단 거리로 갱신
            heappush(pq, (new_cost, next_node))
 
INF = int(1e9)
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    graph = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for d in dirs:
                di = i + d[0]
                dj = j + d[1]
                # 유효범위에 대해
                if 0 <=di <N and 0<=dj<N:
                    # 현재 위치, 다음 위치, 다음 위치 복구 비용을 저장
                    graph[i][j].append(((i, j), (di, dj), board[di][dj]))
 
    costs = [[INF]*N for _ in range(N)]
    dijkstra((0, 0))
    print(f'#{tc} {costs[N-1][N-1]}')