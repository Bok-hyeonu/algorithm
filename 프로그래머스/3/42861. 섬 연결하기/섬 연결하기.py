# 크루스칼 알고리즘 이용
# n : 섬의 개수, costs : 각 다리를 건설하는 데 들어가는 비용 리스트
def solution(n, costs):
    adjl = [[] for _ in range(n)] # 연결 리스트
    min_v = 0 # 다리 건설 최소 비용
    costs.sort(key = lambda x : (x[2], x[0], x[1])) # 건설 비용 순으로 정렬
    parents = [i for i in range(n)] # 부모 노드 표시
    i = 0 # costs 리스트의 인덱스
    answer = 0 # 건설 비용
    while any(parents): # 모든 섬이 연결될 때까지
        if parents[costs[i][0]] != parents[costs[i][1]] : # 두 섬이 이를 수 있는 또 다른 경로가 없는 경우
            answer += costs[i][2] # 다리 건설
            # 두 섬 중 번호가 작은 쪽을 부모로
            if parents[costs[i][0]] < parents[costs[i][1]]: 
                chi = parents[costs[i][1]] # 자식으로 들어갈 부모 정보 저장 
                par = parents[costs[i][0]] # 부모 정보 저장
                parents[costs[i][1]] = parents[costs[i][0]]
            else:
                chi = parents[costs[i][0]]
                par = parents[costs[i][1]]
                parents[costs[i][0]] = parents[costs[i][1]]
            # 자식이 된 부모 중에서 자식이 있었으면
            for j in range(n):
                if parents[j] == chi:
                    parents[j] = par
        else: # 또 다른 경로가 있으면 다음 건설비용 다리 탐색
            i += 1
    return answer