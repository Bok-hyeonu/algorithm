def dfs(x, y, d):
    global memo

    if x == N-1 and y == N-1:      # 목표 지점에 도달한 경우
        return 1

    if memo[x][y][d] != -1:        # 이미 방문한 적이 있는 경우 저장된 값을 사용
        return memo[x][y][d]

    cnt = 0

    # 파이프가 가로
    if d == 0:
        if y+1 < N and board[x][y+1] == 0:  # 가로로 한 칸 이동 가능한 경우
            cnt += dfs(x, y+1, 0)
        if x+1 < N and y+1 < N and board[x+1][y] == board[x][y+1] == board[x+1][y+1] == 0:  # 대각선으로 이동 가능한 경우
            cnt += dfs(x+1, y+1, 2)

    # 파이프가 세로로
    elif d == 1:
        if x+1 < N and board[x+1][y] == 0:  # 세로로 한 칸 이동 가능한 경우
            cnt += dfs(x+1, y, 1)
        if x+1 < N and y+1 < N and board[x+1][y] == board[x][y+1] == board[x+1][y+1] == 0:  # 대각선으로 이동 가능한 경우
            cnt += dfs(x+1, y+1, 2)

    # 파이프가 대각선
    elif d == 2:
        if y+1 < N and board[x][y+1] == 0:  # 가로로 한 칸
            cnt += dfs(x, y+1, 0)
        if x+1 < N and board[x+1][y] == 0:  # 세로로 한 칸
            cnt += dfs(x+1, y, 1)
        if x+1 < N and y+1 < N and board[x+1][y] == board[x][y+1] == board[x+1][y+1] == 0:  # 대각선으로 이동 가능
            cnt += dfs(x+1, y+1, 2)

    memo[x][y][d] = cnt  # 메모이제이션
    return cnt

N = int(input())  # 집의 크기
board = [list(map(int, input().split())) for _ in range(N)]  # 집의 정보
memo = [[[-1] * 3 for _ in range(N)] for _ in range(N)]  # 메모이제이션을 위한 배열

print(dfs(0, 1, 0))  # 초기 위치는 (0, 1), 초기 방향은 가로(0)
