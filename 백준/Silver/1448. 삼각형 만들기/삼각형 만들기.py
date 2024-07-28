# 1448. 삼각형 만들기


# 1. 각 빨대의 길이를 정렬한다.
# 2. 빨대의 길이가 긴 세 개부터 출발하여 각 빨대의 길이가 
# 삼각형 변의 길이의 조건을 충족하는 경우 종료한다.
# 3. 해당 세 변의 길이의 합이 최댓값이다.

import sys
input = sys.stdin.readline
N = int(input())
straws = [int(input()) for _ in range(N)]
straws.sort(reverse=True)

result = -1     # 세 변의 길이 합
for i in range(N-2):
  # 삼각형 세 변의 길이의 합 조건을 만족시키는 경우 종료 후 출력
  if straws[i] < straws[i+1] + straws[i+2]:
    result = straws[i] + straws[i+1] + straws[i + 2]
    break

print(result)