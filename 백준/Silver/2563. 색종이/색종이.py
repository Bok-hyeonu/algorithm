import sys
N = int(sys.stdin.readline())           # N : 색종이의 수
board = [[0]*100 for _ in range(100)]   # 도화지(비어 있다는 것을 0으로 표시)
for i in range(N):
    # x : 색종이 왼쪽 변과 도화지 왼쪽 변 사이의 거리. 곧 x좌표
    # y : 색종이 아래쪽 변과 도화지 아래쪽 변 사이의 거리. 곧 y좌표
    x, y = map(int, sys.stdin.readline().split())
    # 색종이로 도화지를 덮음. (채워져 있다는 것을 1로 표시)
    for dx in range(x, x+10):
        for dy in range(y, y+10):
            board[dx][dy] = 1

# 도화지에 덮인 색종이의 넓이 구하기
result = 0 # 넓이를 출력
# 각 가로변에 칠해진 색종이의 넓이를 모두 더함
for i in range(100):
    result += sum(board[i])

print(result) 