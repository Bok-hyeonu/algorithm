def dfs(start):
    if start == 99: # 99를 만났으면 1 반환
        return 1
    else:
        visit[start] = 1 # 방문 표시
        for next in (lst1[start], lst2[start]): # 연결된 점들을 방문
            if next != -1 and not visit[next]: # 연결된 점이고, 방문하지 않았다면
                if dfs(next): # 해당 점을 탐색하고 99면 
                    return 1 # 1 반환

for tc in range(1, 11):
    T, E = map(int, input().split())
    edges = list(map(int, input().split()))  # 간선의 순서쌍
    lst1 = [-1] * 100  # 데이터 저장을 위한 크기 100의 배열
    lst2 = [-1] * 100  # 2개
    visit = [0] * 100
    for i in range(E):  # 데이터 저장
        v1, v2 = edges[i * 2], edges[i * 2 + 1]
        if lst1[v1] == -1:
            lst1[v1] = v2
        else:
            lst2[v1] = v2

    result = 1 if dfs(0) else 0 # 찾았으면 1 못 찾았으면 0
    print(f'#{tc}', result)