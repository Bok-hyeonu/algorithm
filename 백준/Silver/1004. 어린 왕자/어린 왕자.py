import math
import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
  x1, y1, x2, y2 = map(int,input().split())

  n = int(input())
  
  count = 0 

  for j in range(n):
    cx, cy, r = map(int, input().split())
    
    d1 = math.sqrt((x1-cx) ** 2 + (y1-cy) ** 2)
    d2 = math.sqrt((x2-cx) ** 2 + (y2-cy) ** 2)

    if d1 < r and d2 > r:
      count += 1
    elif d1 > r and d2 < r:
      count += 1
    elif d1 < r and d2 < r:
      pass
    elif d1 > r and d2 > r:
      pass
  
  print(count)