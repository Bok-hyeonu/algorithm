H, W = map(int, input().split())            # 세로, 가로
blocks = list(map(int, input().split()))    # 블록들의 높이

max_heights = [0]*W                         # 고일 수 있는 최대 물의 높이
max_heights[0] = blocks[0]                  # 좌우 끝 값은 해당 값으로 지정
max_heights[-1] = blocks[-1]
 
total = 0                                   # 고이는 물의 총량
max_left = blocks[0]                        # 좌측 최대(시작 0)
max_right = blocks[-1]                      # 우측 최대(시작 -1)

# 먼저 각 위치에서 좌측 최대값을 저장
for i in range(1 , W-1):
    max_heights[i] = max_left
    max_left = max(max_left, blocks[i]) # 최대 높이 탐색
    
# 그 다음 우측에서의 최댓값과 비교해서 작은 값을 저장
for i in range(W-1, 0, -1):
    max_heights[i] = min(max_heights[i], max_right)
    max_right = max(max_right, blocks[i])

# 최대 높이에서 해당 블록의 높이를 뺌, 양수인 경우만 빗물 증가
for i in range(W):
    total += max(0, max_heights[i]-blocks[i])

print(total)