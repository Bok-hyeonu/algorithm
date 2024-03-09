import sys
# 냅색 알고리즘을 이용한 풀이
N, K = map(int, sys.stdin.readline().split()) # N : 물건의 수, K : 배낭의 용량
# N개의 물건을 받음
stuffs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 편의를 위해 무게 0, 가치 0의 물건을 추가 
stuffs.insert(0, (0, 0)) 

# 냅색 알고리즘을 위한 판(N+1 by K+1 사이즈)(값으로는 가치를 저장함)
dp = [[0]*(K+1) for _ in range(N+1)] 

now_wei = 0 # i번째 물건까지의 합

# N개의 물건에 대해
for i in range(1, N+1):
    wi = stuffs[i][0] # 물건의 무게
    vi = stuffs[i][1] # 물건의 가치
    now_wei += wi
    cmp = min(now_wei, K)
    for j in range(1, cmp + 1):
        # 가방의 무게가 i번째 물건의 무게보다 낮은 경우에는 i번째 물건을 넣을 수 없음
        if j < wi:
            dp[i][j] = dp[i-1][j]
        # 가방의 무게가 i번째 물건의 무게와 같아지는 순간부터
        # i번째 물건의 무게를 빼고 i번째 물건을 넣는 것의 가치와
        # i번째 물건을 넣지 않는 것의 가치를 비교해 더 큰 가치를 저장
        else:
            dp[i][j] = max(dp[i-1][j-wi] + vi, dp[i-1][j])
    # i번째 물건까지의 합을 넘어서는 경우는 i번째 물건까지 다 넣은 경우이므로 가치가 증가하지 않음
    for j in range(now_wei + 1, K + 1):
        dp[i][j] = dp[i][now_wei]

sys.stdout.write(f'{dp[N][K]}\n') # 가치합의 최댓값 출력
