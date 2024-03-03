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
    else:
        for j in range(N):
            # 사용하지 않은 무게추라면
            if used[j] == 0:
                used[j] = 1
                f(i + 1, k, l + weis[j], r, total - weis[j])
                if l >= r + weis[j]: # 우측에 무게를 올릴 수 있는 경우
                    f(i+1, k, l, r + weis[j], total - weis[j])
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