def f(i, total):
    global cnt
    # 모든 경우의 수를 탐색했다면
    if i == N:
        # 목표 수인지 탐색
        if total == S:
            cnt += 1
        return
    # 아직 탐색할 것이 남은 경우
    else:
        f(i+1, total)               # 빼고 할건지
        f(i+1, total+numbers[i])    # 넣고 할건지

N, S = map(int, input().split())            # 정수의 개수, 목표 수
numbers = list(map(int, input().split()))   # 수열
if S == 0: cnt = -1                         # 공집합의 부분수열이
else: cnt = 0                               # 0인 경우 제외
f(0, 0)
print(cnt)