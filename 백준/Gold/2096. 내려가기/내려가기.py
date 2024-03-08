import sys
# 1. 메모리 제한 이슈로 인해 투입하는 대로 연산을 진행한다.
# 2. 최대 비용의 경우와 최소 비용의 경우를 나누어 연산을 진행한다.
# 3. DP와 유사하나 기존의 DP와 달리 memoization은 이전 줄까지만 기록된다.
N = int(sys.stdin.readline()) # 줄의 수
# 각 열의 최소, 최대 비용
min1 = min2 = min3 = max1 = max2 = max3 = 0
for _ in range(N):
    col1, col2, col3 = map(int, sys.stdin.readline().split())
    # 최대 비용 계산
    if max1 > max2:             # 1열이 2열보다 큰 경우
        if max2 > max3:         # 2열이 3열보다 큰 경우(1열이 최대)
            max3 = max2 + col3
            max2 = max1 + col2
            max1 = max1 + col1
        else:                   # 3열이 2열보다 큰 경우(1, 3열 비교)
            if max1 > max3:     # 1열이 최대인 경우
                max3 = max3 + col3
                max2 = max1 + col2
                max1 = max1 + col1
            else:               # 3열이 최대인 경우
                max1 = max1 + col1
                max2 = max3 + col2
                max3 = max3 + col3
    else:                       # 2열이 1열보다 큰 경우
        if max2 > max3:         # 2열이 3열보다 큰 경우(2열이 최대)
            max1 = max2 + col1
            max3 = max2 + col3
            max2 = max2 + col2
        else:                   # 3열이 2열보다 큰 경우(3열이 최대)
            max1 = max2 + col1
            max2 = max3 + col2
            max3 = max3 + col3
    # 최소 비용 계산
    if min1 < min2:             # 1열이 2열보다 작은 경우
        if min2 < min3 :        # 2열이 3열보다 작은 경우(1열이 최소)
            min3 = min2 + col3
            min2 = min1 + col2
            min1 = min1 + col1
        else:                   # 3열이 2열보다 작은 경우(1, 3열 비교)
            if min1 < min3:     # 1열이 최소
                min3 = min3 + col3
                min2 = min1 + col2
                min1 = min1 + col1
            else:               # 3열이 최소
                min2 = min3 + col2
                min3 = min3 + col3
                min1 = min1 + col1
    else:                       # 2열이 1열보다 작은 경우
        if min2 < min3:         # 2열이 3열보다 작은 경우(2열이 최소)
            min3 = min2 + col3
            min1 = min2 + col1
            min2 = min2 + col2
        else:                   # 3열이 2열보다 작은 경우(3열이 최소)
            min1 = min2 + col1
            min2 = min3 + col2
            min3 = min3 + col3
# 최대 최소 출력
sys.stdout.write(f'{max(max1, max2, max3)} {min(min1, min2, min3)}\n') 