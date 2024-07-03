import sys
sys.setrecursionlimit(100000)


from collections import defaultdict

# DFS 함수(재귀)
# 현재의 정점으로부터 가장 먼(합산 비용이 가장 큰) 정점을 찾는 DFS 함수
def dfs(node, distance):

    global max_distance, farthest_node
    # 현재 정점을 방문 처리
    visited[node] = True
    # 만약 현재까지 합산한 비용이 최대 비용보다 크면,
    # 최대 비용을 갱신시키고 함수를 호출한 시작 노드로부터 가장 비용이 큰 노드를 가장 먼 노드로 설정
    if distance > max_distance:
        max_distance = distance
        farthest_node = node
    # 트리에 연결된 다른 정점 중에서 방문하지 않은 정점을 방문 (dfs)
    for next_node, weight in tree[node]:
        if not visited[next_node]:
            dfs(next_node, distance + weight)

# 입력 받기
V = int(input())

# 키에러 방지를 위한 defaultdict 자료 구조 사용
tree = defaultdict(list)

# V개의 트리 정점 정보를 입력받음
for _ in range(1, V):
    data = list(map(int, input().split()))
    parent = data[0]

    for i in range(1, len(data)-2, 2):
        child = data[i]
        weight = data[i+1]
        # 인접 리스트로 풀이, 부모와 자식 모두에게 서로의 정점 및 비용 정보를 입력함
        tree[parent].append((child, weight))
        tree[child].append((parent, weight))

# 첫 번째 DFS
visited = [False] * (V + 1)
max_distance = 0
farthest_node = 1
dfs(1, 0)

# 두 번째 DFS
visited = [False] * (V + 1)
max_distance = 0
dfs(farthest_node, 0)

print(max_distance)
