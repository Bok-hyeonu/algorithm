N = int(input())
arr = [[0 for _ in range(1001)] for _ in range(1001)] # 


def num_arr(x, y, xn, yn, board, k): # 
    for i in range(x, x+xn): # 
        for j in range(y, y+yn):
            board[i][j] = k

    return board


for k in range(1, N+1):
    a, b, an, bn = map(int, input().split()) # 좌표
    arr = num_arr(a, b, an, bn, arr, k) # 색종이 칠하기

for i in range(1, N+1):
    print(sum([lst.count(i) for lst in arr])) # 칠해진 색종이 면적 구하기