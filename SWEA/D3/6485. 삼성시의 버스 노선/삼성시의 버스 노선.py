T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 버스 노선 수
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    P = int(input()) #
    C = [0]*P
    result_C = [0]*P
    for i in range(P):
        C[i] = int(input())
    for i in range(P):
        for j in range(N):
            if A[j] <= C[i] <= B[j]:
                result_C[i] += 1
     
    print(f'#{test_case} ', end='')
    print(*result_C)