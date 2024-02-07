T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')

    N = int(input())

    lst = [[] for _ in range(N)]
    lst[0] = [1]
    print(1)

    for i in range(1, N):
        # 윗 줄의 왼쪽 오른쪽 값을 더해 대입.
        # [0, *lst[i-1]][a] : 왼쪽 값, 첫 열 1을 계산하기 위해 첫 항에 0을 삽입
        # [*lst[i-1], 0][a] : 오른쪽 값, 마지막 열 1을 계산하기 위해 마지막에 0을 삽입
        lst[i] = [[0, *lst[i - 1]][a] + [*lst[i - 1], 0][a] for a in range(i + 1)]
        print(*lst[i])