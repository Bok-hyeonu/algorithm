# 1967. 트리의 지름

# 1. 트리 정보를 입력 받는다. 부모 자식을 신경 쓰지 않는다.
# 2. DFS 탐색으로 1번 노드에서 탐색을 진행한다. 루트 노드로부터 가장 먼 노드를 찾는다
# 3. 루트 노드에서 가장 먼 노드를 시점으로 하여 해당 노드에서 가장 먼 노드를 찾는다
# 4. 그 거리를 출력한다.

import sys
input = sys.stdin.readline
n = int(input())    # 노드의 개수
sys.setrecursionlimit(10**9)

tree = [[] for _ in range(n + 1)]

# 트리 입력(양방향)
for _ in range(n - 1):
    p, c, w = map(int, input().split()) # 부모, 자식, 가중치
    tree[p].append((c, w))  
    tree[c].append((p, w))

# dfs 알고리즘
def dfs(start, dis):
    # 다음 노드와 그 가중치
    for next, next_w in tree[start]:
        # 미방문 지점인 경우 현재 위치에서 가중치만큼 더함
        # 사이클이 없으므로 미방문 지점만 탐색
        if distance[next] == -1:
            distance[next] = dis + next_w
            dfs(next, dis + next_w)

distance = [-1]*(n + 1)
distance[1] = 0
dfs(1, 0)       # 한쪽 끝까지 진행

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
# 가장 먼 노드를 시작지점으로 하여 다시 한번 가장 긴 거리를 찾는다.
last_Node = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[last_Node] = 0
dfs(last_Node, 0)

print(max(distance))