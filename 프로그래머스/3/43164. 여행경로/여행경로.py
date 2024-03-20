def solution(tickets):
    n = len(tickets)                            # 티켓의 수
    answer = []                                 # 결과 배열

    def dfs():
        if len(stack) == n+1 :                  # 쌓인 것이 티켓의 수보다 많다면
            answer.append(stack.copy())         # deepcopy

        for i in range(n):                      
            if not visited[i] and stack[-1] == tickets[i][0]:
                visited[i] = 1
                stack.append(tickets[i][1])
                dfs()
                visited[i] = 0
                stack.pop()

    for i in range(n):
        visited = [0] * n
        stack = []
        if tickets[i][0] == "ICN":              # 인천 공항부터 시작
            visited[i] = 1
            stack.append(tickets[i][0])
            stack.append(tickets[i][1])
            dfs()

    return min(answer)