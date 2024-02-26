T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split()) # N : 도시의 크기, M : 한 집이 지불할 수 있는 금액
    board = [list(map(int, input().split())) for _ in range(N)] # 도시
    max_cnt = 0 # 서비스를 제공할 수 있는 최대 집
    for K in range(1, N + 2): # 서비스 범위
        for i in range(N):
            for j in range(N): # (i, j) : 중심 범위
                cnt = 0 # 서비스를 제공 받는 집
                for l in range(-(K-1), K):
                    for m in range(-(K-1), K):
                        # 절댓값의 합이 K보다 작아야 서비스 제공범위 내에 있음
                        if abs(l) + abs(m) < K:
                            di = i + l
                            dj = j + m
                            # 도시 안에 있는 집에 대해
                            if 0<=di<N and 0<=dj<N and board[di][dj] == 1:
                                cnt += 1 # 서비스 제공
                # 손해를 보지 않으면서
                if cnt*M - (K**2+(K-1)**2) >= 0:
                    if max_cnt < cnt: # 서비스를 제공 받는 집의 최댓값
                        max_cnt = cnt # 갱신

    print(f'#{tc}', max_cnt)