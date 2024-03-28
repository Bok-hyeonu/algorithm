from collections import deque
N, M = map(int, input().split())                     # 미로의 행과 열의 개수
board = [list(map(int, input())) for _ in range(N)]  # 미로
dx = [1, 0, -1, 0]                                   # 이동방향 
dy = [0, 1, 0, -1]
visited = [[False for _ in range(M)] for _ in range(N)] # 각 칸의 방문 여부를 나타낼 2차원 리스트 초기화

deq = deque()         # BFS를 위한 deque초기화, 시작 지점 추가
deq.append((0, 0))    # 시작 지점은 (0, 0)
visited[0][0] = True  # 시작 지점 방문 표시

while deq:
    x, y = deq.popleft()   # deque에서 좌표를 하나 꺼내고
    for i in range(4):     # 현재 위치에서 네 방향 모두 확인
        nx = x + dx[i]     # 다음 x 좌표 계산
        ny = y + dy[i]     # 다음 y 좌표 계산

        # 다음 위치가 미로 범위 내에 있고, 이동 가능하며, 아직 방문하지 않았다면
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and not visited[nx][ny]:
            board[nx][ny] = board[x][y] + 1  # 현재 칸까지의 거리에 1을 더해 갱신

            visited[nx][ny] = True  # 다음 위치를 방문했음 표시
            deq.append((nx, ny))    # 다음 위치를 deque에 추가, BFS 계속 진행
print(board[N-1][M-1])              # # 도착 지점까지의 최단 거리