# 21608 상어 초등학교
# 1. 각 학생이 좌석을 정할 때 유망도를 조사한다.
# 2. 인접 학생 수, 인접 빈 좌석 수, 행, 열 번호
# 3. 우선순위가 높은 순서대로 유망도를 정렬한다.
# 4. 유망도가 가장 높은 좌석에 배정
# 5. 좌석 배정 이후 각 좌석들을 순회하며, 선호도 점수 총 합을 계산
# 5-1. 인덱싱을 편하게 하기 위해 학생들을 번호순으로 정렬
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우
N = int(input()) # 칸의 수
board = [[0]*N for _ in range(N)]           # 판
students = [list(map(int, input().split())) for _ in range(N**2)]

for student in students:
    possibles = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:         # 주인 없는 자리만 탐색
                continue

            my_pick, empty = 0, 0   # 내 픽과 빈 칸
            for d in dirs:          # 해당 자리의 상하좌우를 탐색
                di = i + d[0]
                dj = j + d[1]
                # 유효범위 내에서
                if 0 <= di < N and 0 <= dj < N:
                    # 내 픽이 인접한 자리이면 내 픽 + 1
                    if board[di][dj] in student[1:]:
                        my_pick += 1
                    # 빈 칸이면 빈 칸의 수 + 1
                    elif board[di][dj] == 0:
                        empty += 1
            possibles.append((my_pick, empty, i, j))
    # 내 픽과 빈 칸의 수는 내림차순, 행, 열 번호는 오름차순으로 우선순위
    possibles.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))     
    board[possibles[0][2]][possibles[0][3]] = student[0]


students.sort()         # 학생 인덱싱을 편리하게 하기 위해 정렬

preferences = 0         # 선호도 계산

for i in range(N):
    for j in range(N):  # 각 좌표의 학생에 대해 인접 선호 학생의 수를 조사
        cnt = 0
        for d in dirs:
            di = i + d[0]
            dj = j + d[1]
            if 0<=di<N and 0<=dj<N:
                if board[di][dj] in students[board[i][j]-1][1:]:
                    cnt += 1
        if cnt <= 1:    # 점수 계산
            preferences += cnt
        else:
            preferences += 10 ** (cnt-1)

print(preferences)