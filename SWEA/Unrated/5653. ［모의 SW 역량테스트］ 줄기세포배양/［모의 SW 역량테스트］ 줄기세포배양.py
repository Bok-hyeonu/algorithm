T = int(input())
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
for tc in range(1, T + 1):
    N, M, K = map(int, input().split()) # 세로, 가로, 배양시간
    Kp = K if K % 2 == 0 else K + 1
    board = [[0]*(M+Kp) for _ in range(N+Kp)] # 보드 생성
    xy_list = [] # 세포가 배양된 셀
    for i in range(Kp//2, Kp//2 + N):
        cells = list(map(int, input().split()))
        for j in range(M):
            # 활성 여부(0, 1, 2), 소요시간, 생명력
            if cells[j] != 0:
                board[i][Kp//2+j] = [1, 0, cells[j]]
                xy_list.append((i, Kp//2+j)) # 셀 리스트에 추가
    
    for k in range(K): # K시간 동안
        new_cells = []
        for xy in xy_list: # 세포들에 대해
            cell = board[xy[0]][xy[1]]
            # 비활성 상태인 경우
            if cell[0] == 1: 
                # 비활성 시간이 모두 끝났으면
                if cell[1]+1 == cell[2]:
                    board[xy[0]][xy[1]] = [2, 0, cell[2]] # 활성 상태로
                else:
                    board[xy[0]][xy[1]][1] += 1
            # 활성 상태인 경우
            elif cell[0] == 2:
                if cell[1] == 0: # 번식해야 하는 경우
                    cell[1] = 1
                    for d in dirs:
                        dx = xy[0] + d[0]
                        dy = xy[1] + d[1]
                        # 빈 셀인 경우
                        if board[dx][dy] == 0: 
                            board[dx][dy] = [1, 0, cell[2]]
                            new_cells.append((dx, dy))
                        # 빈 셀이 아닌 경우 중 방금 이번 턴에 만들어 진 경우
                        elif (dx, dy) in new_cells: 
                            # 현재 생명력이 더 큰 경우 생명력 갱신
                            if cell[2] > board[dx][dy][2]:
                                board[dx][dy][2] = cell[2]
                    if cell[2] == 1: # 생명력이 1인 경우
                        board[xy[0]][xy[1]][0] = 0 # 죽음
                else:
                    # 죽어야 하는 경우
                    if cell[1]+1 == cell[2]:
                        board[xy[0]][xy[1]][0] = 0
                    else:
                        board[xy[0]][xy[1]][1] += 1
        
        xy_list += new_cells # 세포 배양 셀에 추가
    
    # 살아 있는 줄기세포 카운트
    cnt = 0
    for xy in xy_list:
        if board[xy[0]][xy[1]][0] != 0:
            cnt += 1
    
    print(f'#{tc}', cnt)