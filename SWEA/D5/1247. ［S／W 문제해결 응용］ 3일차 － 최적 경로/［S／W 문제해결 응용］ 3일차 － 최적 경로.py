def f(i, k, p, s): # p : 현위치(현재 좌표), s : 현재까지 이동 거리
    global min_t
    if i == k: # 집으로 돌아오기만 하면 되는 경우
        # 현 위치에서 집까지의 거리를 더해줌
        s += abs(p[0]-home[0]) + abs(p[1]-home[1])
        # 최소 여부 조사
        if min_t > s:
            min_t = s
    elif min_t <= s: # 이미 최단 거리를 넘어선 경우
        return
    else:
        for j in range(k): # N명의 고객에 대해
            # P[j] : j번 고객에 방문 여부
            if P[j] == 0:
                P[j] = 1
                # p[0] : 현 위치의 세로 좌표
                # p[1] : 현 위치의 가로 좌표
                # path[j*2] : i번째 고객의 세로 좌표
                # path[j*2+1] : i번째 고객의 가로 좌표
                f(i+1, k, (path[j*2], path[j*2+1]), s + abs(p[0]-path[j*2])+abs(p[1]-path[j*2+1]))
                P[j] = 0
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    path = list(map(int, input().split()))
    comp = (path[0], path[1]) # 출발지인 회사의 좌표
    home = (path[2], path[3]) # 도착지인 집의 좌표
    P = [0]*N # 순열 역할을 할 고객 번호 리스트
    min_t = 1e9 # 최단 거리
    path = path[4:] # 고객들의 좌표
    f(0, N, comp, 0) # 회사부터 출발
    print(f'#{tc}', min_t) # 최단 거리 출력