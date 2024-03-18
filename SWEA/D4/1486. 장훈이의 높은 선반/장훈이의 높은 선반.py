def top_hei(i, hei):
    global min_v
    # 합이 목표 높이 이상이면
    if hei >= B:
        # 높이 차 최소 탐색
        if hei - B < min_v:
            min_v = hei - B
        return
    # 목표 높이 미만이면
    else:
        # 남은 원소들에 대해 하나씩 값을 더하거나 말거나
        for j in range(i+1, N+1):
            top_hei(j, hei+Hs[j-1])


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split()) # N : 점원의 수, B : 선반의 높이
    Hs = list(map(int, input().split())) # 점원들의 키

    min_v = 1e9 # 높이 차이의 최솟값
    top_hei(0, 0)
    print(f'#{tc} {min_v}')