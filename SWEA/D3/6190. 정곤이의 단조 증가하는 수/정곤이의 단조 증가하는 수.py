T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    res = -1
    for i in range(N-1):
        for j in range(i+1, N):
            n = A[i]*A[j]
            n2 = n
            if res > n2:
                continue
            while n > 0:
                t1 = n % 10
                n //= 10
                t2 = n % 10
                if t2 > t1:
                    break
            else:
                res = n2
    print(f'#{tc}', res)  