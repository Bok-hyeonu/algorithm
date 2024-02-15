T = int(input())
for tc in range(1, T + 1):
    # N : 손님의 수, M : K개의 붕어빵 제작에 필요한 시간
    # K : 1회 제작 가능한 붕어빵의 수
    N, M, K = map(int, input().split())
    arrives = list(map(int, input().split()))
    arrives.sort()
    now_s = 0  # 현재 시간
    front = 0 # 시작
    rear = N - 1 # 끝
    result = 'Possible'
    # 모든 손님에 대해
    while front != rear + 1:
        # front + 1 : 붕어빵 순번
        # arrives[front]//M : 해당 손님이 도착했을 때 진기가 종료한 작업 수
        # K : 1회 작업당 붕어빵
        # 결국 해당 손님이 왔을 때 만들어진 붕어빵의 수가 손님의 순번보다
        # 적으면 Impossible
        if front + 1 > (arrives[front] // M) * K:
            result = 'Impossible'
            break
        front += 1

    print(f'#{tc}', result)