dirs = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
# SWEA 5644. 무선 충전
T = int(input())
for tc in range(1, T + 1):
    # M : 이동 시간, A : 충전기의 개수
    M, A = map(int, input().split())
    path_a = [0]
    path_b = [0]
    path_a += list(map(int, input().split())) # A의 이동 정보
    path_b += list(map(int, input().split())) # B의 이동 정보
    board = [[0]*10 for _ in range(10)]
    charges = []
    for _ in range(A):
        # x, y 충전기의 위치, c : 충전 범위, p : 충전량
        charges.append(list(map(int, input().split())))
    pos_a = [1, 1]
    pos_b = [10, 10]
    ch_a = 0 # A 충전량
    ch_b = 0 # B 충전량
    # 충전 범위가 겹치는 경우 가장 높은 두 범위에서 충전
    for i in range(M+1):
        # 위치 조정
        pos_a[0] += dirs[path_a[i]][0]
        pos_a[1] += dirs[path_a[i]][1]
        pos_b[0] += dirs[path_b[i]][0]
        pos_b[1] += dirs[path_b[i]][1]
        max_a = max_b = sec_a = sec_b = 0
        max_ap = max_bp = sec_ap = sec_bp = 0
        for j in range(A):
            # 각 충전소까지의 거리 계산
            d_a = abs(pos_a[0] - charges[j][0]) + abs(pos_a[1] - charges[j][1])
            d_b = abs(pos_b[0] - charges[j][0]) + abs(pos_b[1] - charges[j][1])
            
            if d_a <= charges[j][2]:
                # 아직 인접한 충전소가 없는 경우
                if max_a == 0: 
                    max_ap = j + 1 # 충전소 번호
                    max_a = charges[j][3] # 충전량 저장
                # 인접한 충전소가 있고 그 충전소보다 충전량이 크거나 같은 경우
                elif max_a <= charges[j][3]:
                    sec_a = max_a
                    sec_ap = max_ap
                    max_ap = j + 1
                    max_a = charges[j][3]
                # 두 번째 충전소보다 충전량이 크거나 같은 경우
                elif sec_a <= charges[j][3]:
                    sec_ap = j + 1
                    sec_a = charges[j][3]
            # B와 거리 계산
            if d_b <= charges[j][2]:
                # 아직 인접한 충전소가 없는 경우
                if max_b == 0: 
                    max_bp = j + 1 # 충전소 번호
                    max_b = charges[j][3] # 충전량 저장
                # 인접한 충전소가 있고 그 충전소보다 충전량이 크거나 같은 경우
                elif max_b <= charges[j][3]:
                    sec_b = max_b
                    sec_bp = max_bp
                    max_bp = j + 1
                    max_b = charges[j][3]
                # 두 번째 충전소보다 충전량이 크거나 같은 경우
                elif sec_b <= charges[j][3]:
                    sec_bp = j + 1
                    sec_b = charges[j][3]
        # 모든 계산을 마친 후
        # 두 충전소가 다른 충전소이면
        if max_ap != max_bp:
            ch_a += max_a
            ch_b += max_b
        # 같은 충전소이면, 두 충전소의 두 번째 충전소 비교
        elif sec_a > sec_b: # A 충전소 충전량이 많은 경우
            ch_a += sec_a
            ch_b += max_b
        else:
            ch_a += max_a
            ch_b += sec_b
    
    print(f'#{tc}', ch_a + ch_b)