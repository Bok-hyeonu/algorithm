def f(i, k):
    global cnt
    if i == k:
        cnt += 1
    else:
        for j in range(N):
            if j not in col[:i]: # 같은 세로 줄에는 퀸을 놓을 수 없음
                if (i+j) not in re[:i]: # 반대각 줄에는 퀸을 놓을 수 없음
                    if (i-j) not in fo[:i]: # 정대각 줄에는 퀸을 놓을 수 없음 
                        fo[i] = i-j # 정대각
                        re[i] = i+j  # 반대각
                        col[i] = j # 열
                        f(i+1, k)
# 정대각 : 행 좌표 - 열 좌표 값이 같은 것이 있으면 정대각 방향에 걸려 놓을 수 없음
# 반대각 : 행 좌표 + 열 좌표의 값이 같은 것이 있으면 반대각 방향에 걸려 놓을 수 없음
# 해당 열 : 같은 세로 줄에는 놓을 수 없음

N = int(input()) # 보드의 크기와 퀸의 수
col = [0]*N
re = [0]*N
fo = [0]*N
cnt = 0
f(0, N)
print(cnt)