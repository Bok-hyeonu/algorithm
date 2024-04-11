# 백준 3190. 뱀
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 보드의 크기 입력 및 보드 생성
N = int(input())
board = [[0]*N for _ in range(N)]

# 사과의 개수
K = int(input())

# 사과의 위치 입력
apples = []
for _ in range(K):
    R, C = map(int, input().split())
    apples.append((R-1, C-1))
    board[R-1][C-1] = 1

# 방향 변환 횟수 입력 및 변환 정보 저장
L = int(input())
change_dirs = {}
for _ in range(L):
    change_time, change_dir = input().split()
    # change_time 초가 끝난 뒤에 방향 전환을 하므로, 시간에 +1을 해줌
    change_dirs[int(change_time)+1] = change_dir
# 좌표
start = (0, 0)

# 자신의 몸에 닿으면 게임을 끝내야하기 때문에, 몸의 좌표를 전부 저장해야함
# 저장해서 움직이는 몸의 좌표는 q
q = deque([start])
time = 0
d = 0

while q:
    time += 1
    # 현재 시간에 방향전환을 해야하면, D/L 여부에 따라 방향 전환을 해줌
    if time in change_dirs:
        if change_dirs[time] == 'D':
            d += 1
        else:
            d -= 1

    # 우선 머리 좌표와 방향을 기준으로 다음 머리 좌표를 구하고 유효성 검사 실시
    cur = q[-1]
    di, dj = cur[0] + dirs[d%4][0], cur[1] + dirs[d%4][1]
    # 게임이 종료되는 조건
    if di < 0 or di >= N or dj < 0 or dj >= N or (di, dj) in q:
        break
    # 사과를 먹은 조건에는 머리만 붙임
    elif board[di][dj]:
        q.append((di, dj))
        board[di][dj] = 0
    # 사과를 안먹은 조건에는 꼬리를 떼고 머리를 붙임
    else:
        q.append((di, dj))
        q.popleft()
print(time)