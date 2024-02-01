T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) # 세로, 가로
    board = [list(map(int, input().split())) for _ in range(N)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_pang = 0
    for i in range(N):
        for j in range(M):
            pang = board[i][j]
            for p in range(1, board[i][j] + 1):
                for d in dirs:
                    ni = i + d[0]*p
                    nj = j + d[1]*p
                    if 0 <= ni < N and 0 <= nj < M:
                        pang += board[ni][nj]
            if pang > max_pang:
                max_pang = pang
 
    print(f'#{tc}', max_pang)