for _ in range(1, 11):
    tc = int(input())

    board = [list(map(int,input().split())) for _ in range(100)]
    pos_y = 99
    for x in range(100):
        if board[99][x] == 2:
            pos_x = x
            break

    dir_rl = [(0, -1), (0, 1)]
    dir_u = (-1, 0)
    now_d = dir_u
    while pos_y > 0:
        if now_d == dir_u:
            for d in dir_rl:
                nx = pos_x + d[1]
                if 0 <= nx < 100 and board[pos_y][nx] == 1:
                    now_d = d
                    break
        else:
            nx = pos_x + now_d[1]
            if 0 <= nx < 100 and board[pos_y][nx] == 1:
                pass
            else:
                now_d = dir_u

        pos_x += now_d[1]
        pos_y += now_d[0]

    print(f'#{tc}', pos_x)