import sys
N = int(sys.stdin.readline()) # 노드 수
adjl = [[] for _ in range(N+1)] # 트리 역할
parents = [0]*(N+1) # 부모 노드 기록
parents[0] = parents[1] = 1
for _ in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
# BFS
q = []
q.append(1)
while q:
    t = q.pop(0)
    for adj in adjl[t]:
        if parents[adj] == 0:
            q.append(adj)
            parents[adj] = t

sys.stdout.write("\n".join(map(str, parents[2:])))