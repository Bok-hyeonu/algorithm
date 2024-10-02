import sys
import math
input = sys.stdin.readline

N, R = map(int, input().split())

xList = []
yList = []

for _ in range(N):
    x, y = map(int, input().split())
    
    xList.append(x)
    yList.append(y)

minX = min(xList)
maxX = max(xList)
minY = min(yList)
maxY = max(yList)

cnt = -100
resultX = 0
resultY = 0

for i in range(minX, maxX + 1):
    for j in range(minY, maxY + 1):
        tmp = 0
        for x, y in zip(xList, yList):
            r = math.sqrt((i - x)**2 + (j - y)**2)
            
            if r <= R:
                tmp += 1
                
        if cnt < tmp:
            cnt = tmp
            resultX = i
            resultY = j

print(resultX, resultY)