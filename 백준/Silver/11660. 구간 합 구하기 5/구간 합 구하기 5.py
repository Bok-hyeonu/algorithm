import sys
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        # 위쪽 가장자리 행인 경우
        elif i == 0:
            board[i][j] += board[i][j-1]
        # 왼쪽 가장자리 행인 경우
        elif j == 0:
            board[i][j] += board[i-1][j]
        # 그 외 경우
        else:
            board[i][j] += board[i-1][j] + board[i][j-1]
            board[i][j] -= board[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == 1 and y1 == 1: # 1, 1인 경우
        result = board[x2-1][y2-1]
    elif x1 == 1: # 시작 위치가 첫 번째 줄인 경우
        result = board[x2-1][y2-1] - board[x2-1][y1-2]
    elif y1 == 1: # 시작 위치가 첫 번째 열에 위치한 경우
        result = board[x2-1][y2-1] - board[x1-2][y2-1]
    else: # 그 외인 경우
        result = board[x2-1][y2-1] - board[x1-2][y2-1] - board[x2-1][y1-2] + board[x1-2][y1-2]
    sys.stdout.write(f'{result}\n') 