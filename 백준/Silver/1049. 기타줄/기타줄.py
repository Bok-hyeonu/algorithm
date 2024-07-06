N, M = map(int, input().split()) # 기타줄의 개수, 브랜드의 수
min_pack = 1001
min_one = 1001
for _ in range(M):
    p, o = map(int, input().split())
    if p < min_pack:
        min_pack = p
    if o < min_one:
        min_one = o

if min_one * 6 < min_pack:
    print(min_one*N)
else:
    total = (N // 6)*min_pack
    N %= 6
    if N * min_one < min_pack:
        total += min_one * N
    else:
        total += min_pack
    print(total)