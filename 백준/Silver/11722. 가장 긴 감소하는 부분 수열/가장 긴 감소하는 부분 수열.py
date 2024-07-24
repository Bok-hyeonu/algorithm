# 11722. 가장 긴 감소하는 부분 수열

N = int(input())
nums = list(map(int, input().split()))
DP = [1]*N
for i in range(N):
    for j in range(i+1, N):
        if nums[i] > nums[j]:
            DP[j] = max(DP[j], DP[i]+1)

print(max(DP))