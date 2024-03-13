# 2775 부녀회장이 될테야
T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    apart = [[0]*n for _ in range(k+1)]
    apart[0] = [i for i in range(1, n+1)]
    for i in range(1, k+1):
        apart[i][0] = 1
    
    for i in range(1, k+1):
        for j in range(1, n):
            apart[i][j] = apart[i][j-1] + apart[i-1][j]
    print(apart[k][n-1])