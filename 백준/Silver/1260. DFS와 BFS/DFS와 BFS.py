import sys

# N : 정점의 수, M : 간선의 수, V : 탐색 시작 번호
N, M, V = map(int, sys.stdin.readline().split())
adjl = [[] for _ in range(N+1)]
stack = [0]*(N+1)
visit_s = [0]*(N+1)
q = [0]*(N+1)
visit_q = [0]*(N+1)
top = -1
front = rear = 0

# 인접 리스트로 그래프 형태로 반환
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
for adj in adjl: # 정렬
    adj.sort()

# dfs
top += 1
stack[top] = V
visit_s[V] = 1
print(V, end = ' ')
while True:
    now = stack[top]
    for i in adjl[now]:
        if visit_s[i] == 0:
            top += 1
            stack[top] = i
            visit_s[i] = 1
            print(i, end= ' ')
            break
    else:
        if top != 0:
            top -= 1
        else:
            break
print()
# bfs
rear += 1
q[rear] = V # enque
visit_q[V] = 1 # 방문했음을 표시
while front != rear:
    front = (front + 1) % (N+1)
    now = q[front] # deque
    print(now, end = ' ')
    for i in adjl[now]:
        if not visit_q[i]:
            visit_q[i] = 1 # 모두 방문
            rear = (rear + 1) % (N+1) # 방문한 정점 enque
            q[rear] = i
print()