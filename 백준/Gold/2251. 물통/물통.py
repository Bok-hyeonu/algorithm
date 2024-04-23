# 2251 물통

# 1. 물통이 3개이므로 옮길 수 있는 경우의 수는 3P2 = 6
# 2. 모든 경우의 수에 대해 물 이동 수행
# 3. 물이 빼질 물통에 물이 없거나 세 물통의 물의 양이 일치한 경우가 있던 경우 추가 탐색 X
# 4. 2번의 경우로 더 이상 탐색할 것이 없을 때까지 탐색 진행

# 물의 양을 탐색할 BFS 함수
def BFS():
    # 큐에는 A, B 물의 양이 저장(C는 정해지므로)
    q = [(0, 0)]
    # A, B 방문 여부 저장
    ABw[0][0] = 1
    # C의 물의 양 저장
    Cw.add(water[2])
    while q:
        new_q = []
        for now in q:
            A = now[0]
            B = now[1]
            C = water[2] - A - B
            for move in moving:
                # move[0] : 물이 빼질 물통
                # move[1] : 물이 더해질 물통
                next = [A, B, C]
                # 물이 빼질 물통에 뺄 물이 없는 경우
                if next[move[0]] == 0:
                    continue
                
                # 옮기려는 물통에 물이 넘치는 경우
                if next[move[0]] + next[move[1]] > water[move[1]]:
                    # 부어지는 만큼 물을 빼줌
                    next[move[0]] -= (water[move[1]] - next[move[1]]) 
                    next[move[1]] = water[move[1]]
                # 안 넘치는 경우
                else:
                    next[move[1]] += next[move[0]]
                    next[move[0]] = 0
                # 이미 현재 케이스를 방문한 경우 다른 케이스 확인
                if ABw[next[0]][next[1]]:
                    continue
                # 방문 표시
                ABw[next[0]][next[1]] = 1
                # A, B 물의 양으로 다음 탐색 진행
                new_q.append((next[0], next[1]))
                # A 물통의 물의 양이 0인 경우 정답 집합에 추가
                if next[0] == 0:
                    Cw.add(next[2])
        q = new_q # 다음 깊이 탐색 진행


moving = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]   # 물을 옮기는 경우의 수
water = list(map(int, input().split()))     # 물 배열

# 물의 양 방문 여부를 확인할 배열
ABw = [[0 for _ in range(201)] for _ in range(201)]
Cw = set()

BFS()

# 리스트로 변환 후 정렬
result = list(Cw)
result.sort()
# 출력
print(*result)