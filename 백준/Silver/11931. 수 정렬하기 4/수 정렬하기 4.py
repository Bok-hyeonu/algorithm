import sys
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)
for i in range(N):
    sys.stdout.write(f'{nums[i]}\n')