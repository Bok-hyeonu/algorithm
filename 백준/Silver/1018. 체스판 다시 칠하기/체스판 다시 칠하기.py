# 두 가지의 가능한 정답판에 대해 모두 탐색을 진행
N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]
BW_board = [['B' if (i+j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]
WB_board = [['W' if (i+j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]
min_cnt = 32
# 모든 경우의 수에 대해
for i in range(N-7):
    for j in range(M-7):
        cnt_bw = 0
        cnt_wb = 0
        for ni in range(8): 
            for nj in range(8):
                if board[i+ni][j+nj] == BW_board[ni][nj]:
                    cnt_wb += 1
                else:
                    cnt_bw += 1
                if cnt_wb >= min_cnt and cnt_bw >= min_cnt:
                    break
            else:
                continue
            break
        m_cnt = cnt_bw if cnt_bw < cnt_wb else cnt_wb
        if min_cnt > m_cnt:
            min_cnt = m_cnt
            if min_cnt == 0:
                break
    if min_cnt == 0:
        break
print(min_cnt) # 최소값 출력