xy_array = [[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            xy_array[i][j] = 1
tot = 0
for xy in xy_array:
    tot += sum(xy)
print(tot)