# n을 만드는 방법에는 n-1을 만드는 경우에서 1을 더하는 것
# n-2를 만드는 경우에서 2를 더하는 것
# n-3을 만드는 경우에서 3을 더하는 것이 있다.
# 따라서 f(n) = f(n-1) + f(n-2) + f(n-3)
def plus123(n):
    memo = [0]*(n+1)
    memo[0] = 1
    memo[1] = 1
    if n >= 2:
        memo[2] = 2
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]

T = int(input())
for _ in range(T):
    print(plus123(int(input())))