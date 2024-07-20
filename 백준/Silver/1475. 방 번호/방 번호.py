nums = list(map(int, input()))
lst = [0]*10
for i in range(len(nums)):
    if nums[i] == 9:
        nums[i] = 6
    lst[nums[i]] += 1

if lst[6] % 2:
    lst[6] += 1

lst[6] //= 2
print(max(lst))