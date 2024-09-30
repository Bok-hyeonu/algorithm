import sys

# N 입력
# n번 반복해서 리스트 채우기 
# visit 비교 및 기준넘버와 비교 
# 만약 다르다 => 나누기 
n = int(sys.stdin.readline())
arr = [] 
res = [0] * 3
for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))

def check(start_x, start_y, n):
  tmp = arr[start_x][start_y]
  for i in range(n):
    for j in range(n):
      if tmp != arr[start_x + i][start_y + j]:
        return False
  return True

def divide(start_x, start_y, n):
  if check(start_x, start_y, n):
    res[arr[start_x][start_y] + 1] += 1
  else:
    for i in range(3):
      for j in range(3):
        divide(start_x + i * n//3,start_y + j * n//3, n//3)

divide(0,0,n)
for i in range(3):
  print(res[i])