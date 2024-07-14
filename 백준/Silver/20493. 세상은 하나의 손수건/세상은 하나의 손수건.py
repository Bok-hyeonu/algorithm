# 20493. 세상은 하나의 손수건

import sys
input = sys.stdin.readline

# 방향
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, T = map(int, input().split())    # 방향 바꾸는 횟수, 총 거리
x, y, d, t = 0, 0, 0, 0     # x, y, 방향, 총 이동거리

# N개의 변경에 대해
for i in range(N):
    dis, direction = input().split()
    dis = int(dis)              # 이동 거리
    # 이전 방향만큼 이동
    x += dirs[d][0] * (dis - t) 
    y += dirs[d][1] * (dis - t)
    # 총 이동 거리 저장
    t = dis
    # 방향에 맞추어 회전
    if direction == 'right':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4

# 마지막까지 이동
x += dirs[d][0] * (T - t)
y += dirs[d][1] * (T - t)
print(x, y) # 출력