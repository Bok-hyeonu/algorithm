# 각 집을 R, G, B 색상으로 칠할 경우의 최소 비용을 찾아가면서 연산한다.
import sys
N = int(sys.stdin.readline())
homes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # RGB 정보
# 두 번째 집부터
for i in range(1, N):
    for j in range(3):
        # 앞 집과 색이 다르면서 비용이 가장 쌌던 페인트를 고른다.
        homes[i][j] += min(homes[i-1][(j+1)%3], homes[i-1][(j+2)%3])
# 가장 마지막 집이 칠해진 후의 최소 비용을 출력한다.
sys.stdout.write(f'{min(homes[-1])}\n')