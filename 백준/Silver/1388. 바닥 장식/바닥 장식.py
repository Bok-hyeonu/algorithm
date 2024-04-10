# 1388 바닥 장식
# 로직
# 1. 좌상단부터 좌에서 우로, 상에서 하로 탐색을 진행한다.
# 2. 방문하지 않은 타일을 발견한 경우 타일의 수를 1 증가시킨다.
# 3. 타일이 가로 방향인 경우 우측을, 세로 방향인 경우 아래 방향으로 탐색한다.
# 4. 양 끝에 도달하거나, 방향이 다른 타일을 만나면 탐색을 종료한다.
# 5. 모든 타일에 대한 탐색이 끝난 후 타일의 수를 출력한다.

import sys

def DFS(pos):
    di, dj = pos[0], pos[1]     # 행 좌표, 열 좌표
    shape = floors[di][dj]
    if shape == '-':    # 모양이 가로라면
        d = (0, 1)      # 우측 방향 탐색
    else:               # 세로면
        d = (1, 0)      # 아래 방향 탐색
    
    # 타일 방향이 동일할 때까지 탐색
    while True:
        # 다음 방향 탐색
        di += d[0]
        dj += d[1]
        # 더 이상 탐색할 곳이 없으면 탐색 종료
        if di == N or dj == M:
            break
        # 모양이 다르면 탐색 종료
        if floors[di][dj] != shape:
            break
        visited[di][dj] = 1     # 방문 표시
            

N, M = map(int, sys.stdin.readline().split())
floors = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

visited = [[0]*M for _ in range(N)] # 탐색 여부 조사
cnt = 0 # 판자의 개수
# 좌상단부터 좌에서 우로 위에서 아래로 탐색을 진행한다.
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        cnt += 1
        visited[i][j] = 1   # 시작 지점 방문 표시
        DFS((i, j))         # 해당 방향으로 탐색 시작

print(cnt)