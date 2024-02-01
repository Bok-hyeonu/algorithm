board = [[0]*1001 for _ in range(1001)]
N = int(input())
rec_list = [list(map(int, input().split())) for _ in range(N)] # x, y, 너비, 높이
for i in range(N):
    for x in range(rec_list[i][0], rec_list[i][0]+rec_list[i][2]):
        for y in range(rec_list[i][1], rec_list[i][1]+rec_list[i][3]):
            board[x][y] = i + 1

cnt_list = []
for i in range(N):
    cnt = 0
    for j in range(1001):
        cnt += board[j].count(i+1)
    cnt_list.append(cnt)

for cnt in cnt_list:
    print(cnt)