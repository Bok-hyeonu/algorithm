import sys
N = int(sys.stdin.readline())               # N : 기둥의 개수
# 왼쪽 위치와 높이를 받습니다.
pils = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pils.sort()                                 # 정렬(키값은 자동으로 기둥의 왼쪽 값이 기준이 됩니다.)
heights = [row[1] for row in pils]
max_hei = max(heights)
idx = heights.index(max_hei)                # 기둥 높이 최댓값을 갖는 인덱스를 찾습니다.

# 가장 높은 높이의 기둥 하나가 가리키는 넓이에 대해서는 탐색과정에 없으므로 먼저 더해줍니다.
result = max_hei                            
np, nh = pils[0][0], pils[0][1]             # 현재 위치와 최대 높이를 배열의 첫 값으로 저장합니다.

for i in range(1, idx+1):                   # 최대 높이의 전방의 넓이를 구합니다.
    result += (pils[i][0] - np)*nh          # 이전 인덱스 
    if pils[i][1] > nh:                     # 기둥의 높이가 지금까지의 높이보다 높은 경우
        nh = pils[i][1]                     # 기둥의 높이를 변경합니다.
    np = pils[i][0]                         # 현재 기둥의 높이를 저장합니다.

enp, enh = pils[-1][0], pils[-1][1]         # 최대 높이 기둥 후방의 넓이도 같은 방식으로 구해줍니다.
for i in range(N-1, idx-1, -1):
    result += (enp - pils[i][0]) * enh
    if pils[i][1] > enh:
        enh = pils[i][1]
    enp = pils[i][0]

print(result)                               # 결과 출력