# 부분 수열의 합
N, S = map(int, input().split())            # 정수의 개수, 목표 수
numbers = list(map(int, input().split()))   # 수열
cnt = 0                         # 경우의 수
for tar in range(1, 1<<N):
    total = 0                   # 수열의 부분합
    for i in range(N):
        if tar & 0x1:
            total += numbers[i] 
        tar >>= 1
    if total == S:              # 부분합이 목표 수이면 
        cnt += 1                # 경우의 수 증가

print(cnt)