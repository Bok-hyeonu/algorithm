# 10974. 모든 순열

# 모든 순열을 사전 순으로 출력

def dfs(i):
    if i == N:
        print(*P)
        return
    
    for j in range(N):
        if used[j]:
            continue
        used[j] = 1
        P[i] = j + 1
        dfs(i + 1)
        used[j] = 0


N = int(input())
P = [0]*N       # 순열 역할을 할 수
used = [0]*N    # 사용 여부
dfs(0)