def dongcheol(i, p):
    global max_p
    # 기저 조건
    if i == N:
        # 확률곱 비교
        max_p = max(max_p, p)
        return
    # 현재까지 확률곱이 낮을 경우 return
    elif p <= max_p:
        return
    # 다음 직원에 일을 시킨다.
    else:
        for j in range(i, N):
            # 작업을 완료한 일인 경우 배정하지 않음
            P[i], P[j] = P[j], P[i]
            dongcheol(i+1, p*tasks[i][P[i]])
            P[i], P[j] = P[j], P[i]
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 직원의 수
    tasks = [list(map(lambda x:int(x)/100, input().split())) for _ in range(N)]  # 직원들에 할당된 일
    max_p = 0.0             # 최대 확률
    P = [i for i in range(N)]
    dongcheol(0, 1.0)
    print(f'#{tc} {max_p*100:.6f}')