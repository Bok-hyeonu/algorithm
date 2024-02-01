T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열
    rc_list = []
    for i in range(N): # N회 반복
        rows_list = []
        q1 = []
        q2 = []
        q3 = []
        for j in range(N):  # 90도
            q1.append(str(board[-j-1][i])) # 90도 회전시킨 배열의 행
            q2.append(str(board[-i-1][-j-1]))
            q3.append(str(board[j][-i-1]))
        rows_list.append(''.join(q1))
        rows_list.append(''.join(q2))
        rows_list.append(''.join(q3))
        rc_list.append(rows_list)

    print(f'#{tc}')
    for rc in rc_list:
        print(*rc)