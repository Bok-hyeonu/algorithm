# 1. BFS를 이용
# 2. BFS의 깊이가 토마토가 익는데 소요되는 시간
# 3. 다 익지 않은 경우 -1 반환

import sys

dirs = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0,0,-1), (0,0,1)]
M, N, H = map(int, sys.stdin.readline().split()) # M : 가로 토마토, N : 세로 토마토, H : 상자의 높이
tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
day = 0                 # 모두 익을 때까지 소요되는 일 수
fresh = []              # 바로 익은 토마토를 fresh라 표현
for i in range(H):      # 익은 토마토 리스트
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 1:
                fresh.append((i, j, k))

while fresh:            # 바로 익은 토마토가 존재할 때까지
    day += 1            # 소요일 수 + 1
    n_fresh = []        # 이제 익을 토마토
    for tomato in fresh:# 토마토가 주위를 익힘
        for d in dirs:
            di = tomato[0] + d[0]
            dj = tomato[1] + d[1]
            dk = tomato[2] + d[2]
            if 0<=di<H and 0<=dj<N and 0<=dk<M and tomatoes[di][dj][dk]==0:
                tomatoes[di][dj][dk] = 1
                n_fresh.append((di, dj, dk))
    fresh = n_fresh

day -= 1                # 마지막에는 더 이상 익을 토마토가 없었으므로 - 1
result = 0
for i in range(H):      # 익지 않은 토마토가 존재하는 경우 -1 반환
    for j in range(N):
        for k in range(M):
            if tomatoes[i][j][k] == 0:
                day = -1
                result = 1
                break
        if result:
            break
    if result: break

print(day)              # 익는 데 소요되는 일 수 반환