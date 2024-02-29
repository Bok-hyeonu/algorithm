import sys
N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.insert(0, 0)
# 수열을 해당 인덱스 까지의 총합으로 계산
for i in range(2, N+1):
    nums[i] += nums[i-1]

for _ in range(M):
    # i번째부터 j번째까지의 합은 j까지의 총합에서 i-1까지의 총합을 뺀 것
    i, j = map(int, sys.stdin.readline().split())
    sys.stdout.write(f'{nums[j]-nums[i-1]}\n')