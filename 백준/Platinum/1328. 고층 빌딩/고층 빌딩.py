# 1328. 고층 빌딩

# 1. 개념 : 기존에 배치된 상태에서 빌딩을 하나씩 추가하며, 이 빌딩은 높이가 가장 낮다고 가정하자.
# 2. 높이가 가장 낮은 빌딩을 가장 좌측에 배치했는데 이 때 전체 빌딩 수가 i, 좌측에서 보이는 빌딩 수가 j, 우측에서 보이는 빌딩 수가 k라면
#  전체 빌딩 수가 i-1, 좌측에서 보이는 빌딩 수가 j-1, 우측에서 보이는 빌딩 수가 k인 상태에서 가장 좌측에 높이가 낮은 빌딩을 놓은 것이다.(DP[i-1][j-1][k])
# 3. 가장 우측의 경우도 똑같다.(DP[i-1][j][k-1])
# 4. 중간에 위치한 경우는 좌, 우측에서 보이는 빌딩 수는 이전과 동일하다. 그리고 각 i-1개의 빌딩 사이에 위치시킬 수 있으므로 (i-1) - 1개 위치에 빌딩을 놓을 수 있다.
# DP[i - 1][j][k] * (i - 2)

# 빌딩 최대 높이, 가장 왼쪽에서 볼 수 있는 빌딩의 수, 오른쪽에서 볼 수 있는 빌딩의 수
N, L, R = map(int, input().split())
mod = 1000000007    # 나눌 수
# DP 배열 생성
DP = [[[0 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)]
DP[1][1][1] = 1     # 빌딩이 1개이면 놓을 수 있는 경우의 수는 1개

for i in range(2, N + 1):           # 전체 빌딩의 수
    for j in range(1, L + 1):       # 좌측에서 보이는 빌딩 수
        for k in range(1, R + 1):   # 우측에서 보이는 빌딩 수
            DP[i][j][k] = (DP[i-1][j][k]*(i - 2)    # 중간에 배치하는 경우(양 끝에 배치하는 2가지 경우를 제외하고 i-2개 위치에 들어갈 수 있음) 
                            + (DP[i-1][j][k-1]      # 오른쪽에 배치한 경우(오른쪽에서 보이는 빌딩 수가 늘었으므로 이전 상황은 빌딩 1개 우측 1개 적은 상태)
                            + DP[i-1][j-1][k])) % mod   # 좌측에 배치한 경우(좌측에서 보이는 빌딩 수가 늘었으므로 이전 상황은 빌딩 1개 좌측 1개 적은 상태)

print(DP[N][L][R])  