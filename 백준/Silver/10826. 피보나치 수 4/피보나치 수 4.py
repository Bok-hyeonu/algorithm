n = int(input())
if n > 0:
    DP = [0]*(n+1)
    DP[0] = 0
    DP[1] = 1
    for i in range(2, n+1):
        DP[i] = DP[i - 1] + DP[i - 2]
    print(DP[n])
else:
    print(0)