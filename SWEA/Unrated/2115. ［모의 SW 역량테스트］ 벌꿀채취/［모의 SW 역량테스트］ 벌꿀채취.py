# 선택한 벌통에서 얻을 수 있는 최대 이익을 반환하는 함수
def max_honey(pos): # 벌통의 위치
    honeys = board[pos[0]][pos[1]:pos[1]+M] # 벌들
    max_honey = 0
    # 가능한 부분집합에 대해
    for sub in range(1, 1<<M):
        total = 0
        honey = 0
        for i in range(M):
            if sub & 0x1:
                total += honeys[i]
                # 추출한 벌꿀이 허용치를 초과한 경우
                if total > C:
                    break
                honey += honeys[i] ** 2  # 벌꿀로 얻을 수 있는 수익
            sub >>= 1
        if honey > max_honey:
            max_honey = honey

    return max_honey


T = int(input())
for tc in range(1, T + 1):
    # N : 벌통의 사이즈, M : 채취 가능 벌통의 수, C : 1회 채취가능한 최대양
    # 가로로 연속이 되도록 선택
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 선택 가능한 벌통들에서 얻을 수 있는 최대의 이익을 저장
    yields = [[0]*(N-M+1) for _ in range(N)] # 선택 가능한 벌통 조합

    for i in range(N):
        for j in range(N-M+1):
            yields[i][j] = max_honey((i, j))


    # 두 일꾼의 벌통 선택 조합
    result = 0  # 최대 이익 합
    for i in range(N):
        for j in range(N-M+1):
            res_a = yields[i][j]        # 첫 번째 일꾼이 얻은 이익
            # 두 번째 일꾼은 첫 번째 일꾼이 얻은 그 다음의 벌통부터 조회 가능하다.
            # 두 번째 일꾼이 얻은 이익을 합쳐 최대 이익 합 갱신
            for k in range(j+M, N-M+1):
                res_b = yields[i][k]
                if res_a + res_b > result:
                    result = res_a + res_b
            for k in range(i+1, N):
                for l in range(N-M+1):
                    res_b = yields[k][l]
                    if res_a + res_b > result:
                        result = res_a + res_b
    print(f'#{tc} {result}')