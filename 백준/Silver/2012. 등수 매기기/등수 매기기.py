# 2012. 등수 매기기

# 1. 예상 등수를 오름차순 정렬한다.
# 2. 오름차순 정렬한 예상 등수 순으로 1등부터 N등까지 등수를 부여한다.
# 3. 해당 차이를 계산한다.

import sys
input = sys.stdin.readline
result = 0    # 불만도의 합
N = int(input())  # 총 인원 수
expectaions = [int(input()) for _ in range(N)]

expectaions.sort()  # 정렬

for i in range(N):
  # 예상 등수 순으로 1등부터 N등까지 부여 후 해당 차이 계산
  result += abs(i + 1 - expectaions[i])

print(result) # 출력