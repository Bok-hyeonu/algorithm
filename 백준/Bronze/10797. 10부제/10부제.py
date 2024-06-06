num = int(input())
cars = list(map(int, input().split()))
cnt = 0
for car in cars:
    if num == car:
        cnt += 1
print(cnt)