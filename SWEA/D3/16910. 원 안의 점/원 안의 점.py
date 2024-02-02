T = int(input()) # 테스트 케이스
for tc in range(1, T + 1):
    N = int(input()) # 반지름
    cnt = 0 # 포함될 점의 수
    # 하나의 사분면에 포함되는 점의 수 * 4
    # 각 사분면을 나누는 2개의 축에 위치하는 점의 수 : 2*(2*N + 1) - 1
    # X축, Y축, 중복되는 0 - 1
    for i in range(1, N + 1): # 1사분면 기준
        for j in range(1, N + 1):
            if i * i + j * j <= N * N: # 원 내에 위치하는 점이면
                cnt += 1 # 포함될 점의 수 1 증가

    print(f'#{tc}', cnt * 4 + 2*(2*N+1)-1) # 출력
