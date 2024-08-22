N = int(input())
for _ in range(N):
    fore = 'MMM'
    a, b = map(int, input().split())
    if a < b:
        fore = 'NO'
    print(f'{fore} BRAINS')