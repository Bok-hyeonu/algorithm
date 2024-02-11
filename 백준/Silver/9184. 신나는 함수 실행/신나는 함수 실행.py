import sys
w = [[[1 for _ in range(51)] for _ in range(51)] for _ in range(51)]
for k in range(1,51): # a항이 먼저 정립되어야 하므로
    for j in range(1,51): # c항 a항 순서를 변경
        for i in range(1,51):
            if i < j < k: # i < j < k 순이면
                w[k][j][i] = w[k-1][j][i] + w[k-1][j-1][i] - w[k][j-1][i]
            else: # 아니면
                w[k][j][i] = w[k][j][i-1] + w[k][j-1][i-1] + w[k-1][j][i-1] - w[k-1][j-1][i-1]                
    
while True: 
    a, b, c = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1: # 종료 조건
        break
    if a <=0 or b<=0 or c<=0:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = w[20][20][20]
    else:
        result = w[c][b][a]
    
    print(f'w({a}, {b}, {c}) =', result)