N = int(input())
x_min = y_min = 10000
x_max = y_max = -10000
for _ in range(N): # 최대, 최소 구하기
    x, y = map(int, input().split())
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y
# x, y 좌표의 최소와 최대를 좌하, 우상 꼭짓점으로 사각형이
# 모두 포함하며 넓이가 최소
print((x_max-x_min)*(y_max-y_min)) 