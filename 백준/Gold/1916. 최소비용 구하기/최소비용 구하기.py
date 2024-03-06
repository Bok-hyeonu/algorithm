import sys

def get_city():
    idx = 0 # 가장 비용이 덜 드는 도시
    min_v = cost[idx]
    for i in range(1, N+1):
        # 비용이 덜 들고 방문하지 않은 도시인 경우
        if cost[i] < min_v and not visited[i]:
            min_v = cost[i] # 다음 탐색할 도시 갱신
            idx = i 
    return idx  # 도시 번호 반환
    

N = int(sys.stdin.readline()) # 도시의 수
M = int(sys.stdin.readline()) # 노선의 수
adjl = [[] for _ in range(N+1)] # 각 도시가 시점인 노선 리스트 생성
visited = [0]*(N+1)
cost = [1e10+1]*(N+1)
# 모든 노선의 정보 입력
for _ in range(M):
    st, ed, co = map(int, sys.stdin.readline().split()) # 출발, 도착, 비용
    adjl[st].append((ed, co))

start, target = map(int, sys.stdin.readline().split()) # 출발 도시와 도착 도시

cost[start] = 0     # 출발지의 비용은 0
visited[start] = 1  # 방문
# 시작 도시의 노선을 순회하며
for line in adjl[start]:
    # 도착지까지의 비용을 삽입, 같은 노선 여러 개 존재 가능
    if line[1] < cost[line[0]]:
        cost[line[0]] = line[1] 

for i in range(N-1):
    # 방문하지 않은 비용이 가장 적은 도시를 꺼내 방문
    t = get_city()
    visited[t] = 1
    # 도시 t가 출발지인 다른 노선 확인
    for l in adjl[t]:
        n_cost = cost[t] + l[1] 
        # 이 경로가 최소비용인 경우
        if n_cost < cost[l[0]]:
            cost[l[0]] = n_cost
sys.stdout.write(f'{cost[target]}\n') # 도착지까지 이르는 최소비용 출력