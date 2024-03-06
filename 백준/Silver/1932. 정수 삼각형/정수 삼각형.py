import sys

n = int(sys.stdin.readline())
inttri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):       # 1층부터 시작(맨 위층을 0층이라 하자)
    for j in range(i+1):    # i층은 방이 i+1개이다. 
        if j == 0:          # i층의 가장 좌측 방의 경우 i-1층의 가장 좌측 방의 값을 전달받음
            inttri[i][j] += inttri[i-1][j]
        elif j == i:        # i층의 가장 우측 방의 경우 i-1층의 가장 우측 방의 값을 전달받음
            inttri[i][j] += inttri[i-1][j-1]
        else:               # 그 외의 경우, i-1층의 인접한 두 방 중 값이 큰 방의 값을 입력받음
            inttri[i][j] += max(inttri[i-1][j], inttri[i-1][j-1])

print(max(inttri[-1]))      # 가장 아래층의 최댓값 출력