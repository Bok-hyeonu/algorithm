import sys
hor, ver = list(map(int, sys.stdin.readline().split())) # 가로, 세로
hor_list = [0, hor] # 가로 좌표 위치
ver_list = [0, ver] # 세로 좌표 위치
cnt = int(input()) # 자르기 횟수
# 가로로 자를 때는 세로 좌표 위치에 삽입하고
# 세로로 자를 때는 가로 좌표 위치에 삽입해야 함을 주의한다.
while cnt > 0:
    way, pos = list(map(int, sys.stdin.readline().split())) # 방향, 위치
    if way == 0: # 가로 방향일 경우
        ver_list.append(pos) # 자르는 위치 삽입
    else: # 세로 방향일 경우
        hor_list.append(pos) # 자르는 위치 삽입
    cnt -= 1 # 다음 위치

hor_list.sort() # 각 가로 세로의 자르는 위치들을 정렬한다.
ver_list.sort() 
area_list = [] # 넓이 리스트
for i in range(1, len(hor_list)):  # 각 가로, 세로 좌표에 대해
    for j in range(1, len(ver_list)): 
        # 가로, 세로를 곱해 넓이 리스트에 추가한다.
        # 각 가로, 세로는 리스트에서 해당 인덱스에서 이전 인덱스의 값을 뺀 값이다.
        area_list.append((hor_list[i]-hor_list[i-1])*(ver_list[j]-ver_list[j-1]))

print(max(area_list)) # 넓이 중 최댓값을 반환한다.