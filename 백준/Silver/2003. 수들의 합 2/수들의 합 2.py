import sys
# N : 수열의 길이, M : 목표 합
N, M = map(int, sys.stdin.readline().split()) 
arr = [0]
arr += list(map(int, sys.stdin.readline().split()))

# 해당 인덱스까지의 총합 계산 및 탐색 시작 인덱스 계산
st = None               # 탐색 시작 인덱스, 이 인덱스 이전까지의 합으론 M에 도달 불가
for i in range(1, N+1):
    arr[i] += arr[i-1]
    if st == None:
        if arr[i] >= M:
            st = i
cnt = 0                 # 경우의 수
if st:                  # M이 모든 수열의 합보다 큰 경우 탐색 필요 없음
    # i번째 수부터 j번째 수까지의 합은 
    # j번째 수까지의 합에서 i-1번째 수까지의 합을 빼는 것과 같음
    # 이 경우는 경우의 수를 구하는 문제이므로 배열의 가장 앞에 0을 추가할 경우
    # 인덱스를 고려할 필요가 없음
    for i in range(N):
        for j in range(max(st,i+1), N+1):
            # i번째 수부터 j번째 수까지의 합이 목표 합을 넘은 경우
            # j를 늘릴 필요가 없음
            if arr[j] - arr[i] > M: break
            # 값이 같은 경우 경우의 수 증가
            elif arr[j] - arr[i] == M: cnt += 1

sys.stdout.write(f'{cnt}\n')
