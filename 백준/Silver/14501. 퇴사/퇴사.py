# 14501. 퇴사

# 1. 풀이 방법 : DP
# 2. 알고리즘
# 1) i번째 날의 상담을 진행한다고 가정한다.
# 2) i번째 날의 상담이 종료되는 날부터 퇴사날까지의 기존 이익과
# 3) i번째 날까지의 이익 + i번째 날의 상담을 진행했을 때 얻는 이익을 비교하여 최댓값으로 갱신
# 4) N번째 날의 이익은 백준이가 얻을 수 있는 최대 이익이다.

import sys

# 퇴사까지 남은 기간
N = int(sys.stdin.readline())
# 상담 계획
plans = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

profits = [0]*(N+1) # 이익
# 각 날짜에 잡힌 상담 계획을 확인한다.
for i in range(N):
    # i번째 날의 상담 일정을 진행한다고 가정하고
    for j in range(i+plans[i][0], N+1):
        # i번째 날부터 상담이 종료되는 날까지 얻을 수 있는 이익의 최대를 갱신
        profits[j] = max(profits[i]+plans[i][1], profits[j])

print(profits[-1])