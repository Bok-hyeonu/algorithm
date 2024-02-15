import sys

N = int(sys.stdin.readline())
coors = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# sort의 기본 옵션은 키 값 순서대로 오름차순 출력
coors.sort() 
for coor in coors: # 출력
    print(*coor)