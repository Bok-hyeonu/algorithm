# 3190. 뱀

# 고려할 종료 조건
# 1. 벽에 부딪힌 경우(유효범위 밖인 경우)
# 2. 자신의 몸에 부딪힌 경우
# 진행
# 1. 시간이 증가하고 뱀이 이동한다.
# 2. 유효범위가 아니면(벽에 부딪히면) 종료한다.
# 3. 사과가 있으면 길이가 증가한다.
# 4. 자신에 닿으면 종료한다.
# 5. 방향을 바꿔야 하는 경우 변경한다.

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하상좌
import sys
from collections import deque

N = int(sys.stdin.readline()) # 보드의 크기
K = int(sys.stdin.readline()) # 사과의 개수

board = [[0]*N for _ in range(N)]
snakes = [[-5]*N for _ in range(N)]

# 사과의 위치 표시
for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    board[i-1][j-1] = 1 # 사과 표시

L = int(sys.stdin.readline()) # 방향 전환의 수
# 방향 전환
rotating = deque([tuple(sys.stdin.readline().split()) for _ in range(L)])

sec = 0         # 소요 시간
d = 0           # 방향(시작은 우측)
di, dj = 0, 0   # 현재 위치
size = 1        # 뱀의 크기
snakes[di][dj] = sec
while True:
    sec += 1 # 소요 시간 증가
    
    # 뱀 이동
    di += dirs[d][0]
    dj += dirs[d][1]
    
    # 종료조건 1(유효범위가 아닌 경우)
    if not 0<= di < N or not 0<= dj < N:
        break
    
    # 사과가 있으면 길이 증가
    if board[di][dj]: 
        size += 1
        board[di][dj] = 0
    
    # 종료조건 2(현 위치가 본인 몸에 닿은 경우)
    if sec - snakes[di][dj] <= size:
        break
    
    # 뱀 이동 현황 표시
    snakes[di][dj] = sec
    
    # 방향을 바꿔야 한다면 방향 변경
    if rotating:
        if int(rotating[0][0]) == sec:
            info = rotating.popleft()
            if info[1] == 'D':  # 우측 회전
                d = (d+1) % 4
            else:               # 좌측 회전
                d = (d-1) % 4

print(sec)