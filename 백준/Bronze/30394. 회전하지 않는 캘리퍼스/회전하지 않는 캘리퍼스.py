N = int(input())
max_y = -1e10
min_y = 1e10
for _ in range(N):
    x, y = map(int, input().split())
    if y > max_y:
        max_y = y
    if y < min_y :
        min_y = y

print(max_y - min_y)