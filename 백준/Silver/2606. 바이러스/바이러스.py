import sys

N = int(sys.stdin.readline()) # 컴퓨터의 수
M = int(sys.stdin.readline()) # 연결의 수

adjl = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
    
for adj in adjl: # 정렬
    adj.sort()
    
visit_s = [0]*(N+1)
q = [0]*(N+1)
visit_q = [0]*(N+1)
front = rear = cnt = -1 
# cnt : 감염된 컴퓨터의 수. 1번 컴퓨터는 카운트 X

rear += 1
q[rear] = 1 # enque
visit_q[1] = 1 # 방문했음을 표시
while front != rear:
    front = (front + 1) % (N+1)
    now = q[front] # deque
    cnt += 1
    for i in adjl[now]:
        if not visit_q[i]:
            visit_q[i] = 1 # 모두 방문
            rear = (rear + 1) % (N+1) # 방문한 정점 enque
            q[rear] = i
print(cnt) # 출력