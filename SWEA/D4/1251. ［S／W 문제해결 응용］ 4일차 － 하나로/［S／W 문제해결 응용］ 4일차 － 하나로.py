def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 같은 집합이면 pass
    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for tc in range(1, T + 1):
    N = int(input())                        # 섬의 개수
    xs = list(map(int, input().split()))    # 섬의 x좌표
    ys = list(map(int, input().split()))    # 섬의 y좌표
    E = float(input())                      # 세율

    tunnels = []

    # 각 섬과 섬 사이의 연결 비용 추가
    for i in range(N):
        for j in range(i+1, N):
            # 두 섬의 번호, 건축 비용
            tunnels.append((i, j, (xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2))

    tunnels.sort(key = lambda x:x[2]) # 비용 순으로 정렬

    parents = [i for i in range(N)]

    sum_cost = 0            # 총 건설 비용(과세 전)
    cnt = 0                 # 건설 터널의 개수
    for s, e, c in tunnels:
        # 이미 연결되어 있다면 pass
        if find_set(s) == find_set(e):
            continue
        # 연결 되어 있지 않다면 연결
        cnt += 1
        union(s, e)
        sum_cost += c

        if cnt == N-1:      # 건설한 터널의 수가 N-1개이면 종료
            break

    print(f'#{tc} {round(sum_cost*E)}')