# 오셀로 게임
class Othello:
    # 상하좌우 정대각, 반대각(양방향)
    dirs = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

    def __init__(self, n):
        self.board = [[0 for _ in range(n+2)] for _ in range(n+2)]
        self.board_size = n
        self.board[n // 2 + 1][n // 2 + 1], self.board[n // 2][n // 2] = 2, 2 # 백돌
        self.board[n // 2][n // 2 + 1], self.board[n // 2 + 1][n // 2] = 1, 1 # 흑돌

    def __str__(self):
        self.board = [[j for j in i[1:-1]] for i in self.board[1:-1]]
        return f'{self.board}'

    def __len__(self):
        return len(self.board)

    def pprint(self):
        pprint(self.board)

    def do(self, i, j, c): # 착수 작업 i : 행 좌표, j : 열 좌표, c : 돌 색깔
        self.board[i][j] = c # i행 j열에 착수
        dir_lst = [] # 색을 바꿔야 할 방향

        for d in self.dirs: # 모든 방향에 대해
            ni = i + d[0]   
            nj = j + d[1]  
            point = self.board[ni][nj]
            if point != 0 and point != c: # 해당 지점의 색이 다른 색이면
                dir_lst.append(self.dirs.index(d)) # 색 바꿀 방향 리스트에 추가

        self.change_stones(i, j, c, dir_lst) # 색 바꾸는 메서드 실행

        return self.board

    def change_stones(self, i, j, c, dir_lst): # i,j,c 같음, dir_list 색 방향
        for num in range(len(dir_lst)): # 바꿔야 할 방향에 대해
            temp_lst = []
            temp_point = self.board[i][j]
            ni, nj = i, j
            while temp_point:
                ni += self.dirs[dir_lst[num]][0]
                nj += self.dirs[dir_lst[num]][1]
                temp_point = self.board[ni][nj]
                if temp_point == 0: # 바꿀 범위가 지났으면
                    break # 종료
                elif temp_point != c: # 다른 색깔이면
                    temp_lst.append([ni, nj]) # 바꿀 리스트에 추가
                else: # 같은 색을 만난 경우
                    # 바꿀 리스트에 저장된 좌표들을 변경(뒤집음)
                    for e in temp_lst: 
                        self.board[e[0]][e[1]] = c
                    break
        return self.board # 바뀐 결과 반환

    def count_values(self): # 백돌과 흑돌의 개수를 세는 함수
        ones = 0
        twos = 0
        for e in self.board:
            ones += e.count(1)
            twos += e.count(2)
        return ones, twos 


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = Othello(N)

    for _ in range(M):
        x, y, stone = map(int, input().split())
        board.do(x, y, stone)

    result = board.count_values()

    print(f'#{tc}', *result)