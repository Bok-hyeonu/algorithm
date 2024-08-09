N = int(input())

a = N // 5
ispossible = False
# a부터 하나씩 낮추면서
for i in range(a, -1, -1):
    if (N - 5*i) % 2:
        continue
    ispossible = True
    print(i + (N-5*i) // 2)
    break

if not ispossible:
    print(-1)