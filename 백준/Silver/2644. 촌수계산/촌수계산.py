# 2644. 촌수 계산

# 1. 인접리스트 입력
# 2. 방문 여부를 확인할 visited 생성
# 3. BFS 탐색
# 3.1 탐색 성공 시 종료 조건 삽입

import sys
n = int(sys.stdin.readline())   # 전체 사람의 수
start, target = map(int, sys.stdin.readline().split())  # 촌수 계산을 할 두 사람

adjl = [[] for _ in range(n+1)] # 각 관계를 표현할 인접리스트
m = int(sys.stdin.readline())   # 부모-자식 관계 수
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split()) # 부모, 자식
    adjl[x].append(y)
    adjl[y].append(x)

visited = [0]*(n+1)

q = [start]     # 한 쪽 사람에서부터 탐색 시작
cnt = 0         # 촌수
is_find = False # 탐색 성공 여부
while q:
    cnt += 1    # 탐색이 시작되면 1촌
    new_q = []  # 다음 촌수의 사람이 담길 리스트
    # 현재 촌수의 사람들의
    for now in q:
        # 다음 촌수 사람들을 탐색
        for next in adjl[now]:
            # 다음 촌수의 사람들이 이미 이전 촌수에 존재한다면 탐색 X
            if visited[next]:
                continue
            # 원하는 촌수의 사람을 찾은 경우 탐색 성공
            if next == target:
                is_find = True
                new_q = []
                break
            # 찾지 못했다면, 탐색 여부 갱신 및 다음 촌수의 사람으로 추가
            visited[next] = 1
            new_q.append(next)
    q = new_q   # 다음 촌수 사람들 갱신
# 탐색 성공 시 촌수 출력
if is_find:
    print(cnt)
# 실패시 -1 출력
else:
    print(-1)
