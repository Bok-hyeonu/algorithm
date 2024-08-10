N, K = map(int, input().split())

DP = [i for i in range(N+1)]

DP[0] = 1

for i in range(1, N+1):
    DP[i] *= DP[i - 1] 

print((DP[N] // (DP[N-K]*DP[K]))%10007)