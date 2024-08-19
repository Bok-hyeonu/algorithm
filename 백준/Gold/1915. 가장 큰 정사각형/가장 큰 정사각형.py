# 1915. 가장 큰 정사각형

# 1. i행 j열을 우하단 꼭짓점으로 하는 정사각형의 최대 크기를 저장하는 방식으로 접근한다.
# 2. i행 j열을 우하단 꼭짓점으로 하는 정사각형이려면 i행 j열 값이 1이어야 한다.
# 3. i행 j열을 우하단 꼭짓점으로 하는 정사각형이려면 i-1행 j-1열, i-1행 j열, i열 j-1행이 모두 색칠되어 있어야 한다.
# 4. i행 j열을 우하단 꼭짓점으로 하는 정사각형의 최대 크기는 i-1행 j-1열, i-1행 j열, i열 j-1행 을 각각 우하단 꼭짓점으로 하는
#   세 개의 가장 큰 정사각형의 최소 크기 + 1이다. 최소 크기를 따라간다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

for i in range(1, n):   # n행
  for j in range(1, m): # m열
    if board[i][j]:     # i행 j열이 1인 경우
      # 좌, 상, 좌상 세 개의 점을 우하단 꼭짓점으로 하는 정사각형의 최대 크기들의 최솟값 + 1
      board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

# 최댓값을 구하는 과정
max_side = 0
for i in range(n):
  for j in range(m):
    if board[i][j] > max_side:
      max_side = board[i][j]

print(max_side**2)