cheolsu_list = []

lenC = lenR = 5
lenD = lenRD = 1
row_bingo = [1, 2, 3, 4, 5]
col_bingo = [1, 2, 3, 4, 5]
cnt = 0

for _ in range(5): # 철수 리스트
    cheolsu_list += list(map(int, input().split()))

mc_list = []
for _ in range(5): # mc 리스트
    mc_list += list(map(int, input().split()))

for i in range(11): # 11개까진 3빙고가 나오지 않음
    idx = cheolsu_list.index(mc_list[i])
    cheolsu_list[idx] = 0

for i in range(11, 25):
    idx = cheolsu_list.index(mc_list[i])
    cheolsu_list[idx] = 0
    
    # 행
    for row in range(lenR):
        hap = sum(cheolsu_list[(row_bingo[row]-1)*5:(row_bingo[row]-1)*5+5])
        if hap == 0:
            row_bingo.pop(row)
            lenR -= 1
            cnt += 1
            break
            
    # 열
    for col in range(lenC):
        hap = sum(cheolsu_list[(col_bingo[col]-1)::5])
        if hap == 0:
            lenC -= 1
            col_bingo.pop(col)
            cnt += 1
            break
    
    # 정대각
    for dia in range(lenD):
        hap = sum(cheolsu_list[::6])
        if hap == 0:
            cnt += 1
            lenD -= 1
    
    # 반대각
    for dia in range(lenRD):
        hap = sum(cheolsu_list[4:-4:4])
        if hap == 0:
            cnt += 1
            lenRD -= 1
    
    if cnt >= 3:
        print(i+1)
        break