# 창용 마을 무리의 개수
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adjl = [[] for _ in range(N + 1)]
    q = [0]*(N+1)
    front = rear = -1
    visited = [0]*(N+1) # 정점의 방문 여부 탐색
    visited[0] = 1
    # 정점과 정점 연결
    for _ in range(M):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    cnt = 0 # 무리의 개수
    
    # 방문하지 않은 정점이 하나라도 있는 경우
    while not all(visited): 
        # 미방문 정점 탐색
        for i in range(N+1):
            if visited[i] == 0:
                rear += 1
                visited[i] = 1
                q[rear] = i
                cnt += 1
                break
        # 해당 정점을 시작으로 BFS 탐색
        while front != rear:
            front += 1
            t = q[front]
            # 인접 정점 중에서
            for adj in adjl[t]:
                # 방문하지 않은 정점이면
                if visited[adj] == 0:
                    rear += 1
                    q[rear] = adj # enque
                    visited[adj] = 1 # 방문 표시
    
    print(f'#{tc}', cnt)