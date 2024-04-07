# 4963. 주유소
# 1. BFS를 이용해 분리된 무리들의 수를 세는 문제이다.
# 2. 지도의 좌상단부터 시작하여 미방문 위치를 발견한 경우
#    섬의 수를 1 증가시키고 해당 위치를 시작으로 섬을 수색한다.
# 3. 지도의 우하단까지 2를 반복한다.

# 8방향
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
import sys

def BFS(st):
    q = [st]            # 시작 지점 enque
    while q:            # BFS 진행
        new_q = []      # 다음 깊이 리스트
        for pos in q:   # 현재 깊이의 요소들의 8방향을 탐색
            for d in dirs:
                di = pos[0] + d[0]
                dj = pos[1] + d[1]
                # 유효범위이면서 미방문, 바다가 아닌 경우
                if 0<=di<h and 0<=dj<w and not visited[di][dj] and board[di][dj]:
                    visited[di][dj] = 1     # 방문 표시 후
                    new_q.append((di, dj))  # 다음 깊이 리스트에 append
        q = new_q       # 다음 깊이 갱신

while True:
    # 가로, 세로, 섬과 바다 지도
    w, h = map(int, sys.stdin.readline().split())   
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    
    if w==0 and h==0:
        break
    
    visited = [[0]*w for _ in range(h)]     # 각 지점의 방문 여부
    cnt = 0                                 # 섬의 개수
    for i in range(h):                      # 지도를 순회하며
        for j in range(w):                  # 미지의 세계 발견 시
            if visited[i][j]:
                continue
            if board[i][j]:
                visited[i][j] = 1           # 방문 표시
                cnt += 1                    # 섬의 수 1 증가
                BFS((i, j))                 # 해당 위치를 시작으로 섬의 모든 위치 파악
    
    print(cnt)                              # 이 지도에서의 섬의 수 출력