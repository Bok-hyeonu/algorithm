import sys
nums = [int(sys.stdin.readline()) for _ in range(5)]
nums.sort()
print(int(sum(nums)/5)) # 평균
print(nums[2]) # 중앙값