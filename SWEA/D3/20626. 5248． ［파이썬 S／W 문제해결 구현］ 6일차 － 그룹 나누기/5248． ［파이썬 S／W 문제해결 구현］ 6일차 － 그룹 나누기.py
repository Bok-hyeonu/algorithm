T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())            # N : 한 반의 인원, M : 신청서의 수
    p = [i for i in range(1, N+1)]              # 해당 번호의 조장정보를 저장
    apps = list(map(int, input().split()))      # 신청서들

    for i in range(M):    # 신청서의 수 만큼
        n1, n2 = apps[i*2], apps[i*2+1]         # 신청 쌍
        if p[n1-1] != p[n2-1]:                  # 각 조 조장의 번호가 낮은 조에
            if p[n1-1] < p[n2-1]:               # 높은 조가 흡수됨
                cap, sub = p[n1 - 1], p[n2 - 1] # cap : 흡수할 조,
            else:
                cap, sub = p[n2 - 1], p[n1 - 1] # sub : 흡수되는 조
            for j in range(N):                  # 흡수
                if p[j] == sub:
                    p[j] = cap
    p = set(p)                                  # 중복을 제거한 조장의 수가 곧 조의 수
    print(f'#{tc} {len(p)}')