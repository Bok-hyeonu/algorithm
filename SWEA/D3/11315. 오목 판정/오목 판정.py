def gomok(board):
    # 행 검사
    for i in range(N):
        for j in range(N - 4):
            tot = sum(board[i][j:j + 5])
            if tot == 5:
                return 'YES'
                # 열 검사
    for i in range(N - 4):
        for j in range(N):
            tot = sum(board[i + k][j] for k in range(5))
            if tot == 5:
                return 'YES'
    # 정대각 검사
    for i in range(N - 4):
        for j in range(N - 4):
            tot = sum(board[i + k][j + k] for k in range(5))
            if tot == 5:
                return 'YES'
    # 반대각 검사
    for i in range(N - 4):
        for j in range(4, N):
            tot = sum(board[i + k][j - k] for k in range(5))
            if tot == 5:
                return 'YES'

    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 'o' : 있는 칸, '.' : 비어 있는 칸
    board = [list(map(lambda x: 0 if x == '.' else 1, input().strip())) for _ in range(N)]

    print(f'#{tc}', gomok(board))