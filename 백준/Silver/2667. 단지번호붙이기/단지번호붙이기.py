# 2667 단지 번호 붙이기
# 1. 단지 배정을 받지 못한 집을 찾습니다.
# 2. 해당 집을 시작으로 인접한 집들을 dfs 탐색하며 단지들을 지정합니다.
# 3. 단지 내 집들의 수를 append합니다.
# 4. 단지 배정을 받지 못한 집이 없을 때까지 1~3을 반복합니다.
# 5. 단지의 수와 단지 내 집의 수를 오름차순 정렬한 결과를 출력합니다.
import sys

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(sys.stdin.readline())
board = [list(map(int, input())) for _ in range(N)]
st = [0]*(N**2)
top = -1
home_cnt = []
while True:
    result = 0                  # 단지 배정받지 못한 집이 남은 경우 1, 없으면 
    for i in range(N):          # 단지 내 배정받지 못한 집을 찾은 경우 종료
        for j in range(N):
            if board[i][j]==1:
                top += 1
                st[top] = (i, j)
                result = 1
                board[i][j] = 0
                break
        if result: break
    
    if result == 0:             # 모든 단지에 번호를 붙인 경우 종결
        break
    cnt = 1                     # 해당 단지 내 집의 수
    
    while top > -1:             # 스택에 원소가 남아있을 때까지 dfs
        t = st[top] 
        for d in dirs:          # 인접한 방향에 대해
            di = t[0]+d[0]
            dj = t[1]+d[1]
            # 유효범위 내면서 해당 단지의 집이 있으면 enque
            if 0<=di<N and 0<=dj<N and board[di][dj]:
                cnt += 1         # 단지 내 집의 수 1 증가
                top += 1            
                st[top] = (di, dj)
                board[di][dj] = 0
                break
        else:
            top -= 1
    home_cnt.append(cnt)    # 단지 append

home_cnt.sort()             # 단지 내 집의 수 오름차순 정렬
print(len(home_cnt))        # 단지의 개수
for cnt in home_cnt:        # 단지 내 집의 수
    print(cnt)