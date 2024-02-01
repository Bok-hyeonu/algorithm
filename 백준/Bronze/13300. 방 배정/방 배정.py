N, K = map(int, input().split()) # N : 학생 수, K : 방 수
stu_list = [[0]*2 for _ in range(6)]
for i in range(N):
    S, Y = map(int, input().split()) # S : 여 0 남 1, Y : 학년
    stu_list[Y-1][S] += 1 # 해당 학년 성별 인원 + 1

total = 0 # 전체 방 수
for i in range(6): # 학년
    for j in range(2): # 성별
        total += stu_list[i][j]//K # 정원이 차는 방
        if stu_list[i][j] % K != 0: # 정원이 안 차는 방
            total += 1

print(total) 