import sys

N, M = map(int, sys.stdin.readline().split()) # 정점의 수, 간선의 수
adjl = [[] for _ in range(N+1)] # 인접 리스트
visited = [0]*(N+1)
visited[0] = 1
# 인접 리스트로 표현
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
q = [0]*(N*(N+1)//2)
front = rear = -1
rear += 1
q[rear] = 1
cnt = 1
visited[1] = 1

# 하나라도 방문하지 않은 정점이 있으면, 모든 연결 요소를 확인한 것이 아님
while not all(visited):
    # 큐가 비었으면
    if front == rear:
        for i in range(N + 1):
            # 첫 번째로 방문하지 않은 정점에 대해
            if visited[i] == 0: 
                rear += 1
                q[rear] = i
                cnt += 1
                visited[i] = 1
                break
    front += 1 # deque
    t = q[front] 
    for adj in adjl[t]:
        if visited[adj] == 0: # 방문한 정점이 아니면
            rear += 1 # 방문할 정점에 추가
            q[rear] = adj
            visited[adj] = 1

print(cnt)