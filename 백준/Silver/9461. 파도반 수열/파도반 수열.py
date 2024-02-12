T = int(input())
memo = [1] *(101)
memo[4] = memo[5] = 2
for i in range(6, 101): # 점화식
    memo[i] = memo[i-1] + memo[i-5]
    
for tc in range(1, T + 1):
    N = int(input()) # 정삼각형의 수
    print(memo[N])