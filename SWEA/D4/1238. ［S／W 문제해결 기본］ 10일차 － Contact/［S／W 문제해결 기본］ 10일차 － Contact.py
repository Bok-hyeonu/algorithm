def bfs(s):  # 시작정점s
    # 큐
    q = []
    visited = [0] * (101)  # visited
    q.append((s, 0))  # 시작점과 몇 번째로 연락을 받는 사람인지 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 큐가 비워질때까지
        t = q.pop(0)
        # 방문하지 않은 인접 정점에 대해
        for i in adjl[t[0]]: 
            if visited[i] == 0:
                # 현재 점과 몇 번째로 연락을 받았는지 인큐
                q.append((i, t[1] + 1)) 
                # visited에 몇 번째로 연락을 받은 사람인지 표시
                visited[i] = visited[t[0]] + 1
     
    # 마지막 사람에 도달할 때의 연락 횟수
    max_v = max(visited) 
    for i in range(100, -1, -1): # 뒤에서부터 탐색
        if visited[i] == max_v: # 가장 나중에 연락받게 된다면
            return i # 해당 사람을 반환
 
 
for tc in range(1, 11):
    E, S = map(int, input().split())
    arr = list(map(int, input().split()))
    adjl = [[] for _ in range(101)]
     
    for i in range(E // 2):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        if n2 not in adjl[n1]:
            adjl[n1].append(n2)  # 유향 그래프
 
    print(f'#{tc}', bfs(S))