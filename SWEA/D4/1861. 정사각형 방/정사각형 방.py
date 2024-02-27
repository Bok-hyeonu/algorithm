# 방 위치와 방 번호가 다른 것에 유의
T = int(input())

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 1             # 최대 이동 가능한 방의 수
    max_num = board[0][0]   # 해당 방 번호
    # 모든 점에 대해 검사
    for i in range(N):
        for j in range(N):
            pos = (i, j)    # 탐색하는 점
            cnt = 1         # 현 위치의 점이 이동 가능한 방의 수
            while True:
                for d in dirs:  # 상하좌우 모든 방향에 대해
                    di = pos[0] + d[0]  # 방의 세로 위치
                    dj = pos[1] + d[1]  # 방의 가로 위치
                    # 유효범위 안쪽이면서, 현재 방 번호보다 1 큰 방이면
                    if 0<=di<N and 0<=dj<N and board[di][dj] - board[pos[0]][pos[1]] == 1:
                        cnt += 1    # 이동 가능한 방의 수 1 증가
                        pos = (di, dj) # 다음 탐색 위치
                        break # 상하좌우 탐색 종료
                else: # 상하좌우 모든 방향에 대해 탐색한 결과 방이 없으면
                    break # (i, j) 점 탐색 종료
            # 현 위치에서 이동 가능한 방의 수가 최대 이동 가능한 방의 수보다 큰 경우
            if max_cnt < cnt:
                # 최댓값 및 해당 방 번호 갱신
                max_cnt = cnt
                max_num = board[i][j]
            # 최대 이동 가능한 방의 수와 같고, 방 번호가 작으면 방 번호 갱신
            elif max_cnt == cnt and board[i][j] < max_num:
                max_num = board[i][j]

    print(f'#{tc}', max_num, max_cnt) # 출력