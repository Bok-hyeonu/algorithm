# 크루스칼 알고리즘 이용
# n : 섬의 개수, costs : 각 다리를 건설하는 데 들어가는 비용 리스트
def solution(n, costs):
    costs.sort(key = lambda x : (x[2], x[0], x[1]))         # 건설 비용 순으로 정렬
    parents = [i for i in range(n)]                         # 조상 노드 표시
    i = 0                                                   # costs 리스트의 인덱스
    answer = 0                                              # 건설 비용
    while any(parents):                                     # 모든 섬이 연결될 때까지(모든 섬의 부모가 0번 노드일 때까지)
        if parents[costs[i][0]] != parents[costs[i][1]] :   # 둘의 조상 노드가 다르다 = 두 섬이 이를 수 있는 또 다른 경로가 없다
            answer += costs[i][2]                           # 다리 건설 비용 증가
                                                            # 두 섬의 조상 번호가 작은 쪽을 조상으로
            if parents[costs[i][0]] < parents[costs[i][1]]: 
                chi = parents[costs[i][1]]                  # 자식이 될 노드의 조상 정보를 저장
                par = parents[costs[i][0]]                  # 조상 정보 저장
                parents[costs[i][1]] = parents[costs[i][0]] # 조상 정보 변경
            else:
                chi = parents[costs[i][0]]
                par = parents[costs[i][1]]
                parents[costs[i][0]] = parents[costs[i][1]]
            
            for j in range(n):                              # 자식이 된 노드의 조상들의 다른 자식들이 있었으면
                if parents[j] == chi:                       # 해당 자식들의 조상을 모두 변경
                    parents[j] = par
        else:                                               # 두 섬을 있는 다른 경로가 있는 경우 짓지 않고 다음 비용의 다리 탐색
            i += 1
            
    return answer # 건설 비용 반환
