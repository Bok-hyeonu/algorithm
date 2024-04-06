# 10026. 적록색약
# 1. 적록색약이 아닌 사람이 보이는 구역의 수 BFS(R, G, B)
# 2. 적록색약인 사람이 보이는 구역의 수 BFS(R-G, B)
import sys

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# 적록색약 -> 인접한 빨강 초록이 같은 색으로
def RGB(st, cols):  # cols : 색깔군
    # 첫 좌표 찾기
    q = [st]    # enque
    while q:        # 다음 깊이의 큐가 없을 동안
        new_q = []  # 다음 깊이의 큐 생성
        # 큐에 있는 좌표들의
        for pos in q:
            # 상하좌우를 탐색하며
            for d in dirs:
                di = d[0] + pos[0]
                dj = d[1] + pos[1]
                # 유효범위이면서 미방문 점이며 같은 색깔군이면
                if 0<=di<N and 0<=dj<N and not visited[di][dj] and board[di][dj] in cols:
                    visited[di][dj] = 1     # 방문 표시
                    new_q.append((di, dj))  # enque
        q = new_q   # 큐 갱신
    

N = int(sys.stdin.readline())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

# 비적록색약 구역
visited = [[0]*N for _ in range(N)] # 방문 여부 배열 생성
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        cnt += 1
        RGB((i, j), [board[i][j]])
        
non_cnt = cnt  # 정상 구역 저장
cnt = 0         # 초기화
# 적록색약 구역의 수
visited = [[0]*N for _ in range(N)] # 방문 여부 배열 생성
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        cnt += 1
        if board[i][j]=='B':
            RGB((i, j), ['B'])
        else:
            RGB((i, j), ['R', 'G'])

print(non_cnt, cnt)    # 비적록색약과 적록색약이 보는 구역 생성