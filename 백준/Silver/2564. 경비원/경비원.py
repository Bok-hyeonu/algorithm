wid, hei = map(int, input().split()) # 가로, 세로
N = int(input()) # 상점의 개수
pos_list = []
for i in range(1, N+2):
    d, p = map(int, input().split()) # 방향, 위치
    if d == 1: # 북쪽
        pos_list.append(p)
    elif d == 2: # 남쪽
        pos_list.append(2*wid+hei-p)
    elif d==3: # 서쪽
        pos_list.append(2*(wid+hei)-p)
    else: # 동쪽
        pos_list.append(wid + p)

result = 0 # 상점과 동근 사이 최단 거리 합
pos_d = pos_list.pop() # 동근의 위치
for pos in pos_list: # 상점들을 순회하며
    d1 = abs(pos_d - pos) # 한쪽 방향 거리
    d2 = 2*(hei+wid)-d1
    result += d1 if d1 < d2 else d2 # 그 중 짧은 거리를 더함

print(result)