# 1. 능력치를 보면 행렬 전체의 합이 결국 팀이 가질 수 있는 모든 능력치임을 알 수 있다.
# 2. zip을 이용해 i행과 j열의 합을 계산. i번과 j번이 팀일 때 생기는 모든 능력치들의 합
# 3. 2번의 총합의 절반이 팀이 가질 수 있는 모든 능력치의 합
# 4. NC(N//2)를 구하면 각 번호가 팀일 때의 능력치의 합을 알 수 있다.
# 5. 전체 모든 능력치와 차를 구한다.

import sys
from itertools import combinations

N = int(sys.stdin.readline())                       # 인원 수
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sum_board = [sum(i) + sum(j) for i, j in zip(board, zip(*board))] # 대각선끼리 합
allstat = sum(sum_board) // 2                       # 모든 값 합의 절반
result = 1e9
for l in combinations(sum_board, N//2):             # 대각선 합에서 뽑은 2개 중에서
    result = min(result, abs(allstat - sum(l)))     # 모든 값의 절반 - 그 뽑은 2개 합의 차 = start팀 - link팀
print(result)