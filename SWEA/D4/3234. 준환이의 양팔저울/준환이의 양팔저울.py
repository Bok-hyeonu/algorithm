fact = [1]*9
for i in range(1, 9):
    fact[i] = fact[i-1]*(i+1)

def f(i, k, l, r, total):
    global cnt
    # 우측이 좌측보다 큰 경우 return
    if r > l:
        return        
    
    if i == k:
        cnt += 1
    # 모든 무게를 다 올려도 우측이 더 큰 경우
    elif total + r <= l:
        cnt += fact[k-i-1] * (2**(k-i))
    # 오른쪽에 올릴 필요가 없는 경우
    elif l == r:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                f(i+1, k, l+weis[j], r, total - weis[j])
                used[j] = 0              
    else:
        for j in range(N):
            # 사용하지 않은 무게추라면
            if used[j] == 0:
                used[j] = 1
                for s in range(2): # 양쪽 모두 달아봄(0왼, 1오)
                    f(i+1, k, l + weis[j]*((s+1)%2), r + weis[j]*(s%2), total - weis[j])
                used[j] = 0

# SWEA 3234. 준환이의 양팔저울
# 오른쪽이 왼쪽보다 커져선 안 됨
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    weis = list(map(int, input().split())) # 무게 추
    used = [0]*N
    cnt = 0
    total = sum(weis)
    f(0, N, 0, 0, total)
    print(f'#{tc}', cnt)