import sys

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]       # 방향
N, M = map(int, sys.stdin.readline().split())   # 세로, 가로
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 목표지점 찾기
find = 0                # 탐색 성공. 실패
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            find = 1  # 탐색 성공
            S = (i, j)
            board[i][j] = 0
            break
    if find: break
# 레벨 1인 지점 탐색
first_p = []                            # 1 레벨 지점(1로 표시해야 하는데 갈 수 있는 땅 표시와 겹친다.)
points = []                             # 현재 레벨의 점들
for d in dirs:                          # 목적지의 4방향에 대해 지점 탐색
    di = S[0] + d[0]                    # 최초 지점은 추후 표시해 주어야 함
    dj = S[1] + d[1]
    if 0<=di<N and 0<=dj<M and board[di][dj]:
        board[di][dj] = 0
        first_p.append((di, dj))
        points.append((di, dj))

level = 1                                   
while points:
    level += 1
    n_points = []
    for p in points:                    # 각 점에 대해
        for d in dirs:                  # 상하좌우 중 방문 가능한 점에 대해
            di = p[0] + d[0]
            dj = p[1] + d[1]
            if 0<=di<N and 0<=dj<M and board[di][dj]==1:
                board[di][dj] = level   # 각 지점의 레벨 표시
                n_points.append((di, dj))
    points = n_points                   # 현재 레벨 지점 갱신

# 갈 수 없는 지점 표시
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            board[i][j] = -1

# 레벨 1인 지점 표시
for f in first_p:
    board[f[0]][f[1]] = 1
    
# 출력
for i in range(N):
    print(*board[i])