# 각각의 Ai에 대해 가장 긴 증가하는 수열 길이의 최솟값은 1이다.(자기 자신)
# 뒤에서부터 탐색하며, 나보다 큰 수들이 가지는 가장 긴 증가하는 수열의 길이 중 최댓값에
# 1을 더한 것이 Ai의 가장 긴 증가하는 수열의 길이이다.
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = 1         # 가장 긴 증가하는 수열의 길이
arr2 = [1]*N    # 해당 인덱스의 수를 시작으로 하는 가장 긴 증가 수열의 길이 리스트
for i in range(N-1, -1, -1):
    max_run = 0 # 자신보다 큰 수가 가지는 증가수열의 길이 중 최댓값
    for j in range(i+1, N):
        # 자신보다 큰 수이면
        if arr[i] < arr[j]:
            max_run = max(arr2[j], max_run) # 기존 증가수열 길이의 최댓값과 해당 수의 증가수열 길이의 최댓값을 비교
    arr2[i] += max_run      # 최종적으로 긴 증가수열의 길이를 더 해줌
    res = max(res, arr2[i]) # 가장 긴 증가수열의 길이 최대 갱신
sys.stdout.write(f'{res}')  # 출력