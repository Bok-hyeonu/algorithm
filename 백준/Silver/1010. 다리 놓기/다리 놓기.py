DP = [i for i in range(31)]
DP[0] = 1
for i in range(1, 31):
    DP[i] *= DP[i-1]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(DP[M] // (DP[N]*DP[M-N]))