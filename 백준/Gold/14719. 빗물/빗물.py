# 14719 빗물
# 해당 위치에 물의 고이는 양은
# 양 옆으로 최대 높이 중 작은 값에서 해당 위치의 높이를 뺀 값

H, W = map(int, input().split())            # 세로, 가로
blocks = list(map(int, input().split()))    # 블록들의 높이

total = 0               # 고이는 물의 양의 합
for i in range(1, W-1):
    max_left, max_right = 0, 0
    # 좌측 방향으로의 최대 높이를 구한다.
    for j in range(i-1, -1, -1):
        max_left = max(max_left, blocks[j] - blocks[i])
    # 우측 방향으로의 최대 높이를 구한다.
    for j in range(i+1, W):
        max_right = max(max_right, blocks[j] - blocks[i])
    # 두 최대 높이 중 낮은 값이 해당 위치의 고이는 물의 양
    total += min(max_left, max_right)

print(total)