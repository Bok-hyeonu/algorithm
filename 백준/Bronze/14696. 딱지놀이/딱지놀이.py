N = int(input()) # 라운드
for i in range(N): # N회 싸움
    An, *Ans = map(int, input().split()) # A의 카드
    Bn, *Bns = map(int, input().split()) # B의 카드
    a_c = [0]*4 # 세모, 네모, 동그라미, 별
    b_c = [0]*4 # 세모, 네모, 동그라미, 별 수
    for a in Ans: # A 카운팅
        a_c[a-1] += 1 
    for b in Bns: # B 카드 카운팅
        b_c[b-1] += 1
    idx = 3 # 별 부터 진행
    while idx >= 0: # 모든 카드를 진행하는 동안
        if a_c[idx]==b_c[idx]: # 같으면 다음 순위 카드
            pass
        elif a_c[idx] > b_c[idx]: # a가 더 많으면
            print('A') # A 승
            break
        else: # B가 많으면
            print('B') # B 승
            break
        idx -= 1
    else:
        print('D') # 다 같으면 무승부!!