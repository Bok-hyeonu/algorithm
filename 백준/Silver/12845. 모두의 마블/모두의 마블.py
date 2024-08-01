# 12845. 모두의 마블

# 1. 인접한 카드여야 한다. 
# 2. 업그레이드된 카드의 레벨은 변하지 않는다.

N = int(input())
nums = list(map(int, input().split()))
max_v = max(nums)

print((N-2)*max_v + sum(nums))