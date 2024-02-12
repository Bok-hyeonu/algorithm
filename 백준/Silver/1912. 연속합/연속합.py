n = int(input())
nums = list(map(int, input().split()))
max_v = tot = nums[0]

for i in range(1, n):
    if max_v < 0: # 최댓값이 음수이면
        if nums[i] > max_v: # 현재값이 크기만 하면
            max_v = tot = nums[i] # 최댓값
    else: # 양수이면
        if nums[i] < 0: # 현재 값이 음수인 경우 중
            if nums[i] < -tot: # 더했을 때 합이 음수가 될 경우
                tot = 0 # 0
            else: # 양수일 경우
                tot += nums[i] # 일단 더함
        else: # 현재 값이 양수인 경우엔
            tot += nums[i] # 무조건 더함
        
        if tot > max_v: # 현재 값이 최대보다 크면
            max_v = tot # 변경

print(max_v)