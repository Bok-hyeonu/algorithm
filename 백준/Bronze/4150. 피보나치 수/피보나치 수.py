N = int(input())
if N <= 2:
    print(1)
else:
    DP = [0]*N
    DP[0] = 1
    DP[1] = 1
    for i in range(2, N):
        DP[i] = DP[i-1] + DP[i-2]
    print(DP[-1])
