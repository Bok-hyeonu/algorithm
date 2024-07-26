# 11048. 이동하기

# 1. 각 위치에 도달할때까지 최댓값을 갱신하며 진행
# 2. 우하단 지점까지 반복한 값이 최댓값

import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(1, 0), (0, 1), (1, 1)]   # 이동 가능한 방향

DP = copy.deepcopy(board)         # 배열 복사

for i in range(N):
  for j in range(M):
    for d in dirs:
      di = d[0] + i
      dj = d[1] + j
      # 유효 범위 내에서
      if 0 <= di < N and 0 <= dj < M:
        # 최댓값 갱신
        DP[di][dj] = max(DP[di][dj], board[di][dj] + DP[i][j])

print(DP[N-1][M-1])