T = int(input()) # 테스트 케이스의 수
for tc in range(1, T + 1):
    day, mon, quar, year = map(int, input().split()) # 일일, 월간, 3달, 1년 이용권의 가격
    planned = list(map(int, input().split())) # 연 이용계획
    # 일일 비용 및 월간 비용
    for i in range(12):
        planned[i] *= day
        # 월간 비용보다 큰 경우
        if planned[i] > mon:
            planned[i] = mon
             
    total = sum(planned) # 월간 이용권 적용 시 최소 비용
    # 3달 이용권 경우의 수 탐색
    # 3달 이용권 4개
    total = min(total, 4*quar)
    # 3달 이용권 3개 + 기존 가격 3개
    if total < 3*quar:
        pass
    else:       
        # 한 달 이용권 경우의 수
        for i in range(4):
            for j in range(i, 5):
                for k in range(j, 6):
                    sub = 3*quar
                    p_mon = 0
                    for l in range(6):
                        if l in (i, j, k):
                            p_mon += 2
                        else:
                            sub += planned[l + p_mon] 
                    total = min(total, sub)
    # 3달 이용권 2개 + 기존 가격 6개
    if total < 2*quar:
        pass
    else:
        # 한 달 이용권 경우의 수
        for i in range(7):
            for j in range(i, 8):
                sub = 2*quar
                p_mon = 0
                for l in range(8):
                    if l in (i, j):
                        p_mon += 2
                    else:
                        sub += planned[l + p_mon]
                total = min(total, sub)
                         
    # 3달 이용권 1개 + 기존 가격 9개
    if total < quar:
        pass
    else:
        for i in range(10):
            sub = quar
            p_mon = 0
            for l in range(10):
                if l == i:
                    p_mon += 2
                else:
                    sub += planned[l+p_mon]
            total = min(total, sub)
    # 연간 이용권 비교
    total = min(total, year)
    print(f'#{tc} {total}')