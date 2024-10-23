import sys
input = sys.stdin.readline

n, k = map(int, input().split())

circle = [i for i in range(1, n+1)]
result = []
num = k-1

while len(circle):
    if num >= len(circle):
        num = num % len(circle)
    else:
        result.append(str(circle.pop(num)))
        num += k-1

print("<", ", ".join(result), ">", sep='')