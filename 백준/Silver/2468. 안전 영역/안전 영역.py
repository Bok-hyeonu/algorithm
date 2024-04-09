# 2468. 안전 영역

# 1. 지역의 최소 높이부터, 최대 높이까지를 찾아 그 범위만큼 반복한다.
# 2. 처음부터 순회하며 미방문인 안전지대인 경우, 해당 지점부터 BFS로 이어진 안전지대를 탐색한다.
# 3. 최대 안전 지대의 수를 갱신한다.

import sys
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def safety(st):
    # 주어진 위치를 시작으로 BFS
    q = [st]
    while q:
        new_q = []
        for pos in q:
            for d in dirs:
                di = pos[0] + d[0]
                dj = pos[1] + d[1]
                # 유효범위 + 미방문 + 안전 지대
                if 0<=di<N and 0<=dj<N and not visited[di][dj] and areas[di][dj] > num:
                    visited[di][dj] = 1
                    # 다음 방문지 목록에 추가
                    new_q.append((di, dj))
        q = new_q   # 갱신
    

N = int(sys.stdin.readline()) # 지역의 크기
areas = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

high = 0    # 최대 높이
low = 100   # 최저 높이
for area in areas:
    if max(area) > high:
        high = max(area)
    if min(area) < low:
        low = min(area)

max_safe = 0 # 안전지대의 최대 갯수

for num in range(min(0, low-1), high):
    safe = 0 # 현재 높이에서 안전지대의 수
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 미방문이면서 안전지대인 경우
            if not visited[i][j] and areas[i][j] > num:
                safe += 1           # 안전지대의 수 1 증가
                visited[i][j] = 1   # 방문
                safety((i, j))      # 해당 안전지대 탐색
            else:
                visited[i][j] = 1   # 방문만 표시
    
    if safe > max_safe: # 현재 높이의 안전지대가 최대인 경우 갱신
        max_safe = safe
        
print(max_safe)