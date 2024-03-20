T = int(input())
for tc in range(1, T + 1):
    N = int(input())                # 원자의 수
    moles = [tuple(map(int, input().split())) for _ in range(N)] # 원자들(x, y, 방향, 보유 에너지)
    exploded = [0]*N                # 터졌는지의 여부
    explodable = []

    # 단 둘만 있다는 가정 하에 터질 수 있는 조합인가?
    for i in range(N):
        for j in range(i+1, N):
            # 두 원소가 같은 방향이면 못 만남
            if moles[i][2] == moles[j][2]:
                continue
            # 만날 수 있는 경우
            if moles[i][2] == 0:                                                            # i가 위쪽 방향으로 움직이고(하, 좌, 우 / 1, 2, 3)
                if moles[j][2] == 1:                                                        # j가 아래쪽 방향으로 움직이면
                    if moles[i][0] == moles[j][0] and moles[i][1] < moles[j][1]:            # x좌표가 같고 y좌표가 i가 j보다 작아야 만날 수 있음
                        explodable.append((moles[j][1] - moles[i][1], i, j))                # 폭발 리스트에 추가

                elif moles[j][2] == 2:                                                      # j가 좌측으로 움직이면
                    if moles[j][0] - moles[i][0] == moles[j][1] - moles[i][1] > 0:          # j점이 i점의 우상단(>0)에 위치하면서 좌우 거리와 상하 거리가 같아야 함
                        explodable.append(((moles[j][1] - moles[i][1])*2, i, j))            # 폭발 리스트에 추가

                else:                                                                       # j가 우측으로 움직이면
                    if moles[i][0] - moles[j][0] == moles[j][1] - moles[i][1] > 0:          # j점이 i점의 좌상단(>0)에 위치하면서 좌우 거리와 상하거리가 같아야 함
                        explodable.append(((moles[j][1] - moles[i][1]) * 2, i, j))          # 폭발 리스트에 추가

            elif moles[i][2] == 1:                                                          # i가 아래쪽 방향으로 움직이면(상, 좌, 우 / 0, 2, 3)
                if moles[j][2] == 0:                                                        # j가 위쪽 방향으로 움직이면
                    if moles[i][0] == moles[j][0] and moles[i][1] > moles[j][1]:            # x좌표가 같고 y좌표가 i가 j보다 커야 만날 수 있음
                        explodable.append((moles[i][1] - moles[j][1], i, j))                # 폭발 리스트에 추가

                elif moles[j][2] == 2:                                                      # j가 좌측으로 움직이면
                    if moles[j][0] - moles[i][0] == moles[i][1] - moles[j][1] > 0:          # j점이 i점의 우하단(>0)에 위치하면서 좌우 거리와 상하 거리가 같아야 함
                        explodable.append(((moles[i][1] - moles[j][1]) * 2, i, j))          # 폭발 리스트에 추가

                else:                                                                       # j가 우측으로 움직이면
                    if moles[i][0] - moles[j][0] == moles[i][1] - moles[j][1] > 0:          # j점이 i점의 좌하단(>0)에 위치하면서 좌우 거리와 상하거리가 같아야 함
                        explodable.append(((moles[i][1] - moles[j][1]) * 2, i, j))          # 폭발 리스트에 추가

            elif moles[i][2] == 2:                                                          # i가 좌측으로 움직이고(상, 하, 우 / 0, 1, 3)
                if moles[j][2] == 3:                                                        # j가 우측 방향으로 움직이면
                    if moles[i][1] == moles[j][1] and moles[i][0] > moles[j][0]:            # y좌표가 같고 i의 x좌표가 j의 x좌표보다 커야 함
                        explodable.append(((moles[i][0] - moles[j][0]), i, j))              # 폭발 리스트에 추가

                elif moles[j][2] == 0:                                                      # j가 위로 움직이면
                    if moles[i][0] - moles[j][0] == moles[i][1] - moles[j][1] > 0:          # j점이 i점의 좌하단(>0)에 위치하면서 좌우 거리와 상하 거리가 같아야 함
                        explodable.append(((moles[i][1] - moles[j][1])*2, i, j))            # 폭발 리스트에 추가

                else:                                                                       # j가 아래로 움직이면
                    if moles[i][0] - moles[j][0] == moles[j][1] - moles[i][1] > 0:          # j점이 i점의 좌상단(>0)에 위치하면서 좌우 거리와 상하거리가 같아야 함
                        explodable.append(((moles[j][1] - moles[i][1])*2, i, j))            # 폭발 리스트에 추가

            else:                                                                           # i가 우측으로 움직이고(상, 하, 좌 / 0, 1, 2)
                if moles[j][2] == 2:                                                        # j가 좌측 방향으로 움직이면
                    if moles[i][1] == moles[j][1] and moles[i][0] < moles[j][0]:            # y좌표가 같고 i의 x좌표가 j의 x좌표보다 작아야 함
                        explodable.append(((moles[j][0] - moles[i][0]), i, j))              # 폭발 리스트에 추가

                elif moles[j][2] == 0:                                                      # j가 위로 움직이면
                    if moles[j][0] - moles[i][0] == moles[i][1] - moles[j][1] > 0:          # j점이 i점의 우하단(>0)에 위치하면서 좌우 거리와 상하 거리가 같아야 함
                        explodable.append(((moles[i][1] - moles[j][1]) * 2, i, j))          # 폭발 리스트에 추가

                else:                                                                       # j가 아래로 움직이면
                    if moles[j][0] - moles[i][0] == moles[j][1] - moles[i][1] > 0:          # j점이 i점의 우상단(>0)에 위치하면서 좌우 거리와 상하거리가 같아야 함
                        explodable.append(((moles[j][1] - moles[i][1]) * 2, i, j))          # 폭발 리스트에 추가

    explodable.sort() # 가장 빠른 순으로 정렬
    pre = 0
    result = 0
    pre_lst = []
    for explod in explodable:

        # 시간이 다르면
        if pre != explod[0]:
            # 둘다 소멸되지 않아야 가능
            if exploded[explod[1]] == exploded[explod[2]] == 0:
                result += moles[explod[1]][3]           # 에너지량
                result += moles[explod[2]][3]           # 에너지량
                exploded[explod[1]] = 1
                exploded[explod[2]] = 1
                pre_lst = []
                pre = explod[0]
                pre_lst.append(explod[1])
                pre_lst.append(explod[2])

        # 같으면
        else:
            # 방금 터진게 있는 경우에만
            if not exploded[explod[1]] and explod[2] in pre_lst:
                result += moles[explod[1]][3]           # 에너지량
                exploded[explod[1]] = 1
                pre_lst.append(explod[1])

            if not exploded[explod[2]] and explod[1] in pre_lst:
                result += moles[explod[2]][3]           # 에너지량
                exploded[explod[2]] = 1
                pre_lst.append(explod[2])

    print(f'#{tc} {result}')

