T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    lines.sort() # 전선을 왼쪽 전봇대 기준으로 정렬

    for i in range(N):
        # 본인보다 아래 위치에서 출발하는 전선에 대해
        for j in range(i):
            # 전선의 도착지가 기존 전선의 도착지보다 위인 경우
            if lines[j][1] > lines[i][1]:
                cnt += 1 # 전선의 교차지점 증가

    print(f'#{tc}', cnt)