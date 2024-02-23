import sys
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(sys.stdin.readline())
for i in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    stack = [0]*(k+1) # 하나의 배추 흰 지렁이가 갈 수 있는 좌표
    top = -1
    field = [[0]*n for _ in range(m)]   # 밭 생성
    for i in range(k):                  # 배추 생성
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1
    cnt = 0 # 배추흰지렁이의 수
    # 모든 좌표에 대해 
    for i in range(m):
        for j in range(n):
            # 배추 흰지렁이를 풀지 않은 배추이면,
            if field[i][j] == 1: 
                cnt += 1 # 배추흰지렁이 한 마리 품
                top += 1 # push
                stack[top] = (i, j)
                while top!=-1: # 배추흰지렁이 한 마리가 모든 곳을 돌아다닐 동안
                    pos = stack[top] # pop
                    top -= 1
                    field[pos[0]][pos[1]] = 2 # 배추흰지렁이의 영역임을 표시
                    for d in dirs: # 상하좌우 모든 방향에 대해
                        di = pos[0]+d[0]
                        dj = pos[1]+d[1]
                        # 배추흰지렁이가 갈 수 있는 곳이면
                        if 0<=di<m and 0<=dj<n and field[di][dj] == 1:
                            top += 1 # push
                            stack[top] = (di, dj)
    sys.stdout.write(f'{cnt}\n') # 필요한 배추흰지렁이의 수