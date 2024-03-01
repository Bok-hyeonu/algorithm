import sys

def calcul(perms): # 치킨 거리 계산함수
    global min_d
    
    total_d = 0 # 모든 가구의 치킨 거리 합
    # 모든 집에서 치킨 거리 계산
    for home in homes: 
        d = 100 # 집에서 치킨집까지의 최소 거리(최댓값 100)
        for p in perms: # 치킨집 까지의 거리 계산
            # 집에서 치킨집 p까지의 거리
            c_h = abs(stores[p][0] - home[0]) + abs(stores[p][1] - home[1])
            if c_h == 1: # 거리가 1이면 최소 거리이므로 거리 1
                d = 1
                break # 추가 탐색 필요 X
            # 치킨집 p까지의 거리가 기존 치킨집까지의 최소거리보다 짧다면 갱신
            elif c_h < d: 
                d = c_h
        # 해당 집의 치킨 거리를 치킨 거리 합에 더해줌
        total_d += d
        # 치킨 거리 합이 최소 치킨 거리를 넘어섰다면 추가 탐색 필요 X
        if total_d > min_d:
            return 
    else: 
        min_d = total_d # 최소 치킨 거리라면 최소 치킨거리 갱신
        
# 모든 치킨집 조합을 생성해내는 함수
def f(i, k): 
    if i == k:
        calcul(P)
    elif i == 0:
        for j in range(C - k + 1):
            P[0] = j
            f(1, k)
    else:
        for j in range(P[i-1]+1, C - k + i + 1):
            P[i] = j
            f(i+1, k)
            
# N : 도시의 크기, M : 폐업시키지 않을 치킨집의 수
N, M = map(int, sys.stdin.readline().split())
homes = [] # 집 리스트
stores = [] # 치킨집 리스트
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 도시의 분포
# 집과 치킨 집을 먼저 찾는다.
for i in range(N):
    for j in range(N):
        if board[i][j] == 0: # 빈 공간인 경우
            pass
        elif board[i][j] == 1: # 집인 경우
            homes.append((i, j))
        else: # 치킨집인 경우
            stores.append((i, j))

C = len(stores) # 치킨집의 수

# 치킨집 선택 및 거리 계산
min_d = 1e9 # 최소 치킨 거리
P = [0]*M # 폐업시키지 않을 치킨집 리스트
f(0, M)
sys.stdout.write(f'{min_d}\n')