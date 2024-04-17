# 1253 좋다

# 1. 각 수를 순회하며 
# 2. 자신을 제외한 다른 수 두 개의 합이 자신이 되는지를 확인한다.
# 3. 투 포인터를 활용해 양 끝에서 범위를 줄여가는 방법을 적용한다.

N = int(input())    # 수의 개수
nums = list(map(int, input().split())) # 수의 수
nums.sort()     # 오름차순 정렬

good = 0        # 좋은 수의 개수
for i in range(N):
    find = nums[i]  # 좋은 수가 될지 확인할 수  
    l = 0           # 좌측 포인터
    r = N-1         # 우측 포인터
    while l < r :   # 좌측과 우측 포인터가 만나기 전까지
        # 두 포인터가 가리키는 합이 찾으려는 수이면
        if nums[l] + nums[r] == find:
            # 두 포인터 중 어느 한 포인터도 찾으려는 수를 가리키지 않는 경우만
            # 찾으려는 수가 좋은 수
            if l != i and r != i:
                good += 1
                break
            # 한 포인터가 찾으려는 수를 가리키면 해당 포인터를 이동
            elif l == i:
                l += 1
            else:
                r -= 1
        # 합이 찾으려는 수보다 크면 우측 포인터를 이동
        elif nums[l] + nums[r] > find:
            r -= 1
        # 작으면 좌측 포인터를 이동
        else:
            l += 1
            
print(good)