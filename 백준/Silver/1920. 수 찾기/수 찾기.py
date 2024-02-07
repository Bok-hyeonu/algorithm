N = int(input())
nums = list(map(int, input().split()))
nums.sort()
M = int(input())
nums_m = list(map(int, input().split()))

for i in range(M):
    start = 0
    end = N-1
    while start<=end:
        middle = (start+end)//2
        if nums_m[i]==nums[middle]:
            result = 1
            break
        elif nums_m[i] > nums[middle]:
            start = middle + 1
        else:
            end = middle - 1
    else:
        result = 0
    print(result)