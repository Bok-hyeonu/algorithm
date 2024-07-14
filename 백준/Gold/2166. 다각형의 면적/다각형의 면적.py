# 2166. 다각형의 면적

# 1. 다각형의 면적을 구하는 공식을 이용한다.
# 2. 다각형을 이루는 순서대로 x좌표, y좌표를 나열하고 마지막에 첫번째 x,y 좌표를 추가한다.
# 3. (x1y2 + x2y3 + ... + xny1) - (x2y1 + x3y2 + ... + x1yn) 을 구한다.
# 4. 차의 절댓값을 씌운 후 절반으로 나눈 것을 소숫점 둘째 자리에서 반올림하여 표기한다.

import sys
input = sys.stdin.readline

N = int(input())    # 각의 개수
# 각 점을 입력으로 받음
points = [tuple(map(int, input().split())) for _ in range(N)]
points += [points[0]] # 마지막에 첫번째 x, y 좌표를 추가

x1y = 0 # xiyi+1
xy1 = 0 # xi+1y1

# (x1y2 + ... + xny1), (x2y1 + ... + x1yn)을 구한다.
for i in range(N):
    x1y += points[i][0] * points[i + 1][1]
    xy1 += points[i + 1][0] * points[i][1]

# 그 차의 절댓값을 씌운 것을 절반으로 나눈 것을 출력한다.
print(round(abs(x1y - xy1)/2, 1))