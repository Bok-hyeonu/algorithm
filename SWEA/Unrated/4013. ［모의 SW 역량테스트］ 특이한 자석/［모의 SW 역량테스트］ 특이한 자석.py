T = int(input())
for tc in range(1, T + 1):
    K = int(input()) # 회전 작업 횟수
    # 0이 N, 1이 S
    magnets = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        # num : 자석 번호, d : 회전 방향(1 : 시계, -1 : 반시계)
        num, d = map(int, input().split())
        rotate_list = [(num-1, d)] # 회전시킬 자석의 리스트
        left_d = right_d = d # 회전 방향
        left_blade = magnets[num-1][6] # 좌측 날
        right_blade = magnets[num-1][2] # 우측 날
        left = num - 2 # 왼쪽 자석 번호
        right = num  # 오른쪽 자석 번호
        
        while left >= 0 or right < 4: # 왼쪽이나 오른쪽 탐색할 자석이 남았으면
            ch = 0
            if left >= 0: # 왼쪽 자석 비교
                if left_blade != magnets[left][2]: # 둘의 극이 다를때만
                    rotate_list.append((left, -left_d)) # 반대방향 회전
                    left_blade = magnets[left][6]
                    left -= 1
                    left_d *= -1
                    ch += 1
            
            if right < 4: # 오른쪽 자석 비교
                if right_blade != magnets[right][6]: # 둘의 극이 다른 경우에만
                    rotate_list.append((right, -right_d))
                    right_blade = magnets[right][2]
                    right += 1
                    right_d *= -1
                    ch += 1
            
            if ch == 0:
                break
        
        # 회전
        for r in rotate_list:
            if r[1] == 1: # 시계방향 회전인 경우
                magnets[r[0]] = [magnets[r[0]][-1]] + magnets[r[0]][:7]
            else: # 반시계방향 회전인 경우
                magnets[r[0]] = magnets[r[0]][1:] + [magnets[r[0]][0]]
    
    # 점수 계산
    score = 1
    total = 0
    for magnet in magnets:
        if magnet[0] == 1: # S극이면
            total += score
        score *= 2
    
    print(f'#{tc}', total) # 점수 출력