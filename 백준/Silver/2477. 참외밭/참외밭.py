K = int(input())
d = [(1, 0), (-1, 0), (0, -1), (0, 1)] # 동, 서, 남, 북
pos_x = 0 # 원점 출발
pos_y = 0
pos_xs = [] # x점 리스트
pos_ys = []
for i in range(6): 
    dr, dis = map(int, input().split()) # 방향과 이동거리
    pos_x += d[dr-1][0] * dis # x, y 이동
    pos_y += d[dr-1][1] * dis
    pos_xs.append(pos_x) # 이동된 점 추가
    pos_ys.append(pos_y) 

absent = ['UL', 'UR', 'BL', 'BR'] # 가상의 큰 사각형의 꼭짓점
max_x = max(pos_xs)
min_x = min(pos_xs)
max_y = max(pos_ys)
min_y = min(pos_ys)

max_wid = max_x - min_x # 큰 사각형의 너비
max_hei = max_y - min_y # 큰 사각형의 높이


for i in range(6): # 각 점을 순회하며
    if pos_xs[i] == max_x: 
        if pos_ys[i] == max_y: # 우상단 점이 존재하면
            absent.remove('UR') # 제거
        elif pos_ys[i] == min_y: # 우하단 점이 존재하면
            absent.remove('BR') # 제거
    elif pos_xs[i] == min_x: 
        if pos_ys[i] == max_y: # 좌상단 점이 존재하면
            absent.remove('UL') # 제거
        elif pos_ys[i]==min_y: # 좌하단 점이 존재하면 
            absent.remove('BL') # 제거

for _ in range(2): # 가운데 점을 찾기 위함
    pos_xs.remove(max_x)
    pos_xs.remove(min_x)
    pos_ys.remove(max_y)
    pos_ys.remove(min_y)

if absent[0][0] == 'U': # 존재하지 않는 꼭짓점이 상단이면
    height = (max_y - pos_ys[0])
else:
    height = (pos_ys[0]-min_y)

if absent[0][1] == 'R': # 우측이면
    width = (max_x - pos_xs[0])
else:
    width = (pos_xs[0]-min_x)

print((max_wid*max_hei - height*width)*K) # 넓이 뺀 값 * 참외의 수