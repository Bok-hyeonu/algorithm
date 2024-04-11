# 백준 1388. 바닥 장식

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dirs = {'-': (0, 1), '|': (1, 0)}
cnt = 0

for i in range(N):
    for j in range(M):
        cur = board[i][j]
        if cur:
            cnt += 1
            board[i][j] = False
            di, dj = i, j
            while True:
                di, dj = di + dirs[cur][0], dj + dirs[cur][1]
                if 0 <= di < N and 0 <= dj < M and board[di][dj] == cur:
                    board[di][dj] = False
                else:
                    break

print(cnt)