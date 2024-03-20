def solution(n, edge):
    answer = 0
    visited = [0]*(n+1)
    adjl = [[] for _ in range(n+1)]         # 인접 리스트로 표현
    for e in edge:                  
        adjl[e[0]].append(e[1])
        adjl[e[1]].append(e[0])
        
    queue = [1]
    visited[1] = 1
    while queue:
        answer = len(queue)                     # 마지막 깊이의 정점들의 개수가 결과
        n_queue = []
        for q in queue:
            for w in adjl[q]:                   # 인접 정점
                if not visited[w]:              # 미방문 정점인 경우
                    visited[w] = 1
                    n_queue.append(w)
        
        queue = n_queue
        
    return answer