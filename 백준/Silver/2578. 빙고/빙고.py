row_bingo = [1, 2, 3, 4, 5]
col_bingo = [1, 2, 3, 4, 5]
cnt = rcnt = dcnt = 0

# 철수와 진행자의 빙고판을 각각 1차원 배열로 받습니다.
cheolsu_list = []
mc_list = []
for _ in range(5): # 철수 리스트
    cheolsu_list += list(map(int, input().split()))

for _ in range(5): # mc 리스트
    mc_list += list(map(int, input().split()))

# 3빙고를 위해 최소로 칠해야 할 개수는 12개
for i in range(11): 
    # 따라서 11개까지는 빙고 여부를 판별하지 않음
    idx = cheolsu_list.index(mc_list[i])
    cheolsu_list[idx] = 0 # 일치하는 칸을 칠함

for i in range(11, 25): # 12개 이후부터 판별
    idx = cheolsu_list.index(mc_list[i])
    cheolsu_list[idx] = 0 # 일치하는 칸을 칠함
    
    # 행 조사
    for row in row_bingo: # 아직 빙고가 아닌 가로줄들을 순회하며
        hap = sum(cheolsu_list[(row-1)*5:(row-1)*5+5])
        if hap == 0: # 가로줄이 모두 칠해졌다면
            row_bingo.remove(row) # 해당 가로줄을 빙고 후보에서 제거 
            cnt += 1 # 개수 1 증가
            break # 한 번에 하나의 빙고 밖에 존재하지 않음
            
    # 열 조사
    for col in col_bingo: # 아직 빙고가 아닌 세로줄들을 순회하며
        hap = sum(cheolsu_list[(col-1)::5])
        if hap == 0: # 세로줄이 모두 칠해졌다면
            col_bingo.remove(col) # 해당 세로줄을 후보에서 제거
            cnt += 1 # 빙고 수 1 증가
            break 
    
    # 정대각선(우하향)이 빙고인지 조사
    if  dcnt == 0 and sum(cheolsu_list[::6]) == 0:
        dcnt = 1

    # 반대각선(우상향)이 빙고인지 조사
    if rcnt ==0 and sum(cheolsu_list[4:-4:4]) == 0:
        rcnt = 1
    
    if cnt + rcnt + dcnt >= 3: # 3빙고 이상일 경우 
        print(i+1) # 총 몇 칸을 칠했는지 출력 후 종료
        break