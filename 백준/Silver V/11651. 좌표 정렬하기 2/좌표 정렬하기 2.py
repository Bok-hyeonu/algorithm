import sys
N = int(sys.stdin.readline())
coors = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 키값 순서를 바꾸어 정렬, 내림차순을 하고 싶다면 음수를 취해주면 된다.
coors.sort(key = lambda x: (x[1], x[0])) 
for coor in coors: # 출력
    print(*coor)