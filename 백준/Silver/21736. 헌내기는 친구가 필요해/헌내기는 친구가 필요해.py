# 21736. 헌내기는 친구가 필요해

# 1. 도연이의 위치를 찾는다.
# 2. 도연이의 위치를 시점으로 BFS 탐색을 진행한다.
# 3. 방문한 지점은 재방문하지 않고, 벽으로 막힌 경우 역시 재방문하지 않는다.

import sys
input = sys.stdin.readline

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 방향

# 캠퍼스 크기
N, M = map(int, input().split())            # 세로, 가로
campus = [list(input()) for _ in range(N)]  # 캠퍼스

# 도연이 찾기
isD = False
doyeon = (0, 0)
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            isD = True
            doyeon = (i, j)
            break
    if isD: break

visited = [[0 for _ in range(M)] for _ in range(N) ]
visited[doyeon[0]][doyeon[1]] = 1
# 친구 찾기
q = [doyeon]
friends = 0 # 친구의 수
while q:
    new_q = []
    for t in q:
        for d in dirs:
            dr = d[0] + t[0]
            dc = d[1] + t[1]
            # 유효범위이면서 미방문 점인 경우
            if 0 <= dr < N and 0 <= dc < M and not visited[dr][dc]:
                # 벽이면
                if campus[dr][dc] == 'X':
                    continue
                # 친구면
                if campus[dr][dc] == 'P':
                    friends += 1
                # 방문 표시
                visited[dr][dc] = 1
                # 다음 방문 위치로 추가
                new_q.append((dr, dc))
    q = new_q

if friends:
    print(friends)
else:
    print('TT')