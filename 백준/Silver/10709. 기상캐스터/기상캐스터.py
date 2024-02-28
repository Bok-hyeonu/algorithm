import sys

H, W = map(int, sys.stdin.readline().split()) # 남북, 가로
board = [list(sys.stdin.readline().rstrip()) for _ in range(H)] # 각 구역의 하늘 상태
# 각 지역 순회
for i in range(H):
    cnt = -1                    # 몇 분 후 구름이 드리우는지(안 드리울 경우 -1)
    for j in range(W):
        if board[i][j] == '.':  # 현재 지역이 구름이 없는 경우
            board[i][j] = cnt   # cnt분 뒤에 드리움
                                
            if cnt != -1: cnt += 1 # 구름이 있었으면 +1 없었으면 그대로
        else:                   # 구름이 드리운 경우
            board[i][j] = 0     # 이미 드리워져 있음
            cnt = 1             # 다음 구역은 1분 후 드리울 것임
            
for b in board:                 # 한 줄씩 출력
    print(*b)