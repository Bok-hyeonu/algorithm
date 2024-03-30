# 1. 분할정복 알고리즘으로 풀이합니다.
# 2. 색종이의 좌상단점을 기준으로 하여, 좌상단점과 색깔이 하나라도 다른 경우 4분할
# 3. 해당 색종이 조각의 색이 모두 같으면 해당 색깔 조각의 수를 + 1 해줍니다.
# i, j : 분할된 색종이의 좌상단 행 좌표, 열 좌표, 길이
def partition(i, j, n):
    global w_cnt, b_cnt
    
    color = board[i][j]                     # 좌상단 색종이 한 칸의 색깔
    for ii in range(i, i+n):                # 해당 색종이의 모든 칸에 대해
        for jj in range(j, j+n):
            # 분할 조건
            if board[ii][jj] != color:      # 하나라도 색이 다르다면 색종이를 4분할
                partition(i, j, n//2)       # 좌상단
                partition(i, j+n//2, n//2)  # 우상단
                partition(i+n//2, j, n//2)  # 좌하단
                partition(i+n//2, j+n//2, n//2) # 우하단
                return
    # 모두 색깔이 같은 경우, 색깔에 따라 조각 수 + 1
    if color == 0:  
        w_cnt += 1
    else:
        b_cnt += 1


import sys
N = int(sys.stdin.readline())   # 한 변의 칸 수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 판

b_cnt, w_cnt = 0, 0 # 각 색깔의 조각의 수
partition(0, 0, N)
print(w_cnt)
print(b_cnt)