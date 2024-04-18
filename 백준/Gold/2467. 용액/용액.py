# 2467. 용액

# 1. 알칼리성이나 산성 용액으로만 주어진 경우 특성값이 0에 가까운 두 값의 합이 최소
# 2. 두 성질의 용액이 주어진 경우 좌 우 포인터를 이동하면서 
# 용액의 합의 절댓값의 최솟값을 구한다.
N = int(input())
nums = list(map(int, input().split()))

# 알칼리성 용액이 없으면 특성값이 가장 낮은 두 값의 합이 0에 가장 가깝다
if nums[0] >= 0:
    print(nums[0], nums[1])
# 산성 용액이 없으면 특성값이 가장 높은 두 값의 합이 0에 가장 가깝다
elif nums[-1] <= 0:
    print(nums[-2], nums[-1])
# 그 외의 경우
else:
    left = 0            # 좌측 포인터
    right = N-1         # 우측 포인터
    val_left, val_right = nums[0], nums[-1]  # 최소일 때 좌, 우측의 용액
    min_dif = int(1e9)  # 최솟값
    # 두 포인터가 만날 때까지
    while left < right:
        # 두 포인터가 가리키는 값의 합이 최소이면
        # 최솟값, 좌 우측 용액 갱신
        if abs(nums[left] + nums[right]) <= min_dif:
            min_dif = abs(nums[left] + nums[right])
            val_left = nums[left]
            val_right = nums[right]
            if min_dif == 0:
                break
            
        # 특성값의 절댓값이 큰 쪽의 포인터를 이동
        if abs(nums[left]) > abs(nums[right]):
            left += 1
        elif abs(nums[left]) < abs(nums[right]):
            right -= 1
        # 특성값의 절댓값이 같다면 탐색 종료
        # 부호가 같더라도 지금까지 탐색한 결과가 최소이다.
        else:
            break
    # 좌, 우측값 출력
    print(val_left, val_right)