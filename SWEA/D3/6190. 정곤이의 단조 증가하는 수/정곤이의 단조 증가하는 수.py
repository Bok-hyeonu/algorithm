T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    res = -1
    for i in range(N-1):
        for j in range(i+1, N):
            n = A[i]*A[j]
            num = list(map(int, str(n)))
            for k in range(1, len(num)):
                if num[k] < num[k-1]:
                    break
            else:
                if res < n:
                    res = n
    print(f'#{tc}', res)   