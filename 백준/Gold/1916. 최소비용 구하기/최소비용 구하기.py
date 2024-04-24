from heapq import heappush, heappop
import sys

# 도시, 버스 수 입력
N = int(input())
M = int(input())

# 방문 확인을 할 리스트 생성
visited = [-1] * (N+1)
# 그래프 입력
graph = {}
for i in range(M):
    # 출발 도시, 도착 도시, 비용
    city_from, city_to, weight = map(int, sys.stdin.readline().split())
    if city_from in graph:
        graph[city_from].append((weight, city_to))
    else:
        graph[city_from] = [(weight, city_to)]

# 출발지와 도착지 입력
start, end = map(int, input().split())

# heapq의 요소로 (비용, 도시)를 저장
hq = []
heappush(hq, (0, start))
visited[start] = 0

# heapq에 요소가 있는동안 반복
while hq:
    cur = heappop(hq)
    # 종료 조건
    if cur[1] == end:
        # 여태까지 합해온 비용을 출력
        print(cur[0])
        break
        
    if cur[1] not in graph:
        continue

    for node in graph[cur[1]]:
        next_weight = cur[0] + node[0]
        next_node = node[1]
        # 방문을 안했거나, 방문한 경우 비용이 이전보다 작다면
        if -1 == visited[next_node] or next_weight < visited[next_node]:
            heappush(hq, (next_weight, next_node))
            visited[next_node] = next_weight
        else:
            ...
