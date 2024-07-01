# 2805. 나무 자르기

# 1. 높이를 이진 탐색으로 바꿔가며 상근이가 길이 M인 나무를 확보하며 높이를 최대로 하는 값을 찾는다
# 2. 해당 높이를 출력한다.

N, M = map(int, input().split()) # 나무의 수, 필요한 길이
heights = list(map(int, input().split())) 

left = 1
right = max(heights)

# 최대높이를 찾는 과정
while left <= right:
    total = 0                       # 상근이가 가져가게 되는 나무의 길이
    middle = (left + right) // 2    # 해당하는 경우의 높이
    
    # tree를 순회하며
    for tree in heights:
        if tree > middle:
            total += tree - middle
    # 상근이가 더 가져가야 한다면 자르는 높이를 낮춤
    if total < M:
        right = middle - 1 
    # 상근이가 덜 가져가야 한다면 높이를 높임
    else:
        left = middle + 1

print(right) # 최종 우측 값을 출력한다.
