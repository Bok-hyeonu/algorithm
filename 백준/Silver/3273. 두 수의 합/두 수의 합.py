n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort() # 오름차순 정렬

i = 0
j = n - 1
cnt = 0
while i < j:
    # 목표값과 같다면
    if nums[i] + nums[j] == x:
        cnt += 1
        i += 1
        j -= 1
    # 크다면
    elif nums[i] + nums[j] > x:
        j -= 1
    # 작다면
    else:
        i += 1

print(cnt)