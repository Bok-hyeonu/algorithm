import sys

dirs = {1:(0, -1), 2:(-1, -1), 3:(-1, 0), 4:(-1, 1), 
        5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}

def rainflower(d, s, clouds): # d : 이동 방향, s : 이동거리
    # 1. 모든 구름이 d 방향으로 s칸 이동한다.
    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    m_clouds = []
    for cloud in clouds:
        ni = (cloud[0] + dirs[d][0]*s)%N
        nj = (cloud[1] + dirs[d][1]*s)%N
        board[ni][nj] += 1 # 저장된 물의 양 1 증가
        m_clouds.append((ni, nj))
        
    # 3. 구름이 모두 사라진다.
    # 4. 2에서 물이 증가한 칸에 물복사버그 마법을 시전한다.
    # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니 수만큼 바구니 물의 양이 증가한다.
    # 1, 2에서 한 번에 하지 않은 이유? -> 기존에 물의 양이 0일 수도 있으므로
    for cloud in m_clouds:
        cnt = 0 # 물이 존재하는 바구니 수
        for dd in (2, 4, 6, 8): # 대각 방향에 대해
            di = cloud[0] + dirs[dd][0]
            dj = cloud[1] + dirs[dd][1]
            # 유효범위 내에서 물이 존재하는 경우
            if 0 <= di < N and 0 <= dj < N and board[di][dj] > 0: cnt += 1
        board[cloud[0]][cloud[1]] += cnt
    
    new_clouds = []
    # 5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고 물의 양이 2 줄어든다.
    # 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    # 구름이 아니었던 모든 칸을 조사
    for i in range(N):
        for j in range(N):
            # 구름이 아니었고 바구니에 저장된 물의 양이 2 이상이면
            if board[i][j] >= 2 and (i, j) not in m_clouds:
                board[i][j] -= 2 # 물의 양 2 감소
                new_clouds.append((i, j))
    
    return new_clouds
    
# N : 연습판의 크기, M : 구름 이동 명령 횟수
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 연습판
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)] # 구름의 위치
# M번의 이동 시전
for _ in range(M):
    d, s = map(int, sys.stdin.readline().split()) # d : 이동 방향, s : 이동거리 
    clouds = rainflower(d, s, clouds) # d방향 s거리에 대해 이동 시전

# 모든 이동이 끝난 후 바구니 안의 물 총합 구하기
water = sum(sum(row) for row in board)
print(water)