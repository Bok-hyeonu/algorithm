# 7562. 나이트의 이동

# 1. BFS를 이용하여 출발 위치에서 도착위치까지 가는 최소 이동횟수를 구할 수 있다
# 2. 방문 배열을 생성한다. 
# 3. 출발지로부터 이동횟수가 같은 위치의 점들을 갱신해가며 확인한다.
# 4. 이미 방문한 점인 경우 탐색을 진행하지 않는다.(이동횟수에서 이미 밀린다.)

# 이동방향
dirs = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
import sys

# 이동횟수를 반환하는 함수
def knight(st): # 출발지점
    q = [st]
    cnt = 0                     # 이동횟수
    while q:
        cnt += 1                # 이동횟수 1 증가
        new_q = []
        for pos in q:           # 같은 이동횟수의 점들에 대해
            for d in dirs:      # 나이트가 이동할 수 있는 위치 탐색
                di = pos[0] + d[0]
                dj = pos[1] + d[1]
                # 유효범위이면서 미방문한 경우
                if 0<=di<N and 0<=dj<N and not visited[di][dj]:
                    # 목표지점인 경우 이동횟수 반환
                    if di == tar[0] and dj == tar[1]:
                        return cnt
                    # 목표지점이 아닌 경우 방문 표시 후 다음 경로로 append
                    visited[di][dj] = 1
                    new_q.append((di, dj))
        q = new_q
    return 0

T = int(sys.stdin.readline())                   # 테스트케이스의 수

for _ in range(T):
    N = int(sys.stdin.readline())               # 보드의 크기
    st = tuple(map(int, sys.stdin.readline().split()))      # 시작 지점
    tar = tuple(map(int, sys.stdin.readline().split()))     # 목표 지점
    
    if st[0] == tar[0] and st[1] == tar[1]:     # 출발지와 도착지 일치하면 0
        print(0)
        continue
    visited = [[0]*N for _ in range(N)]         # 방문 여부 
    visited[st[0]][st[1]] = 1
    
    print(knight(st))   # 아니라면 함수 실행