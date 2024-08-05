# 14494. 다이나믹이 뭐에요?

n, m = map(int, input().split())
DP = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    DP[i][0] = 1

for i in range(m):
    DP[0][i] = 1

for i in range(1, n):
    for j in range(1, m):
        DP[i][j] = (DP[i-1][j]  + DP[i][j-1]  + DP[i-1][j-1]) % int(1e9+7)

print(DP[-1][-1])