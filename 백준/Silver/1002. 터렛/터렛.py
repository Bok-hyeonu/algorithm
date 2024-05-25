# 1002. 터렛

# 각 거리를 r1, r2, dis라 할 때, 어느 두 거리의 합 하나 거리보다 
# 짧다면 0, 같다면 1 크다면 2(삼각형 세 변의 길이의 성질을 이용)
# 두 터렛의 위치가 같다면 무한대(-1)

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 위치와 측정 거리가 같다면
    if x1==x2 and y1==y2 and r1==r2:
        print(-1)
    else:
        dis = ((x1-x2)**2+(y1-y2)**2)**(1/2)
        
        # 각 변의 길이를 거리 순으로 정렬
        distances = [dis, r1, r2]
        distances.sort()
        # 가장 긴 변의 길이가 다른 두 변의 길이의 합과 같은 경우
        if distances[2] == distances[1] + distances[0]:
            print(1)
        # 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 큰 경우
        elif distances[2] > distances[1] + distances[0]:
            print(0)
        # 가장 긴 변의 길이가 다른 두 변의 길이의 합보다 작은 경우
        else:
            print(2)