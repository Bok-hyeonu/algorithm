def numberrun(i, pos, seq):
    # 배열의 길이가 7인 경우
    if i == 7:
        num_set.add(seq)
        return
    # 추가할 수가 남은 경우
    else:
        # 상하좌우 유효범위에 대해 탐색 진행
        for d in dirs:
            di = pos[0] + d[0]
            dj = pos[1] + d[1]
            if 0 <= di < 4 and 0 <= dj < 4:
                numberrun(i+1, (di, dj), seq+board[di][dj])
 
 
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
for tc in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]
    num_set = set()
    # 모든 위치에서 돌려주기
    for i in range(4):
        for j in range(4):
            numberrun(1, (i, j), board[i][j])
    # 중복을 제외한 수의 개수
    print(f'#{tc} {len(num_set)}')