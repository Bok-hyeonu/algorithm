dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]   # 하상좌우
for _ in range(10):
    T = int(input())                        # 테스트 케이스
    board = [input() for _ in range(16)]    # 미로판
    queue = []
    queue.append((1, 1))                    # 시작점 삽입
    visit = [[0] * 13 for _ in range(13)]   # 실제 사용되는 board는 (13,13) 사이즈
    result = 0                              # 탐색 실패, 성공 여부 탐색
    while queue:                            # 큐에 원소가 하나라도 있다는 것 = 탐색할 곳이 남아 있다는 것
        t = queue.pop(0)                    # 가장 먼저 저장된 원소를 탐색
        visit[t[0] - 1][t[1] - 1] = 1       # 방문한 것으로 표시
        for d in dirs:                      # 상하좌우 전 방향에 대해
            dy = t[0] + d[0]
            dx = t[1] + d[1]
            # 탐색하는 상하좌우 좌표가 길이 있고 방문하지 않은 곳이라면
            if board[dy][dx] == '0' and visit[dy-1][dx-1] == 0:
                queue.append((dy, dx))      # 해당 좌표 삽입
            elif board[dy][dx] == '3':      # 도착지를 찾은 경우
                result = 1                  # 탐색 성공
                break

    print(f'#{T}', result)