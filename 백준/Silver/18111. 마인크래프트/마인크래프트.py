import sys

N, M, B = map(int, sys.stdin.readline().split()) # 가로, 세로, 인벤토리의 수
floors = [0]*257
# 층 입력
for _ in range(N):
    floor = list(map(int, sys.stdin.readline().split()))
    for cell in floor:
        floors[cell] += 1

total_block = B # 총 블록의 수
for i in range(257):
    total_block += floors[i]*(i)

max_floor = total_block // (N*M) # 일단 가능한 최고 층

for i in range(257):
    if floors[i] != 0: # 가능한 최저 층 도달
        min_floor = i
        break

max_floor2 = min_floor
for i in range(min_floor, 257):
    if floors[i] != 0:
        max_floor2 = i

max_floor = min(max_floor, max_floor2) # 둘 중 작은 값

min_cost = 1e9
result = []
# 최저층부터 최고층까지
for i in range(min_floor, max_floor+1):
    
    cost = 0
    # i : 기준이 되는 층
    # i보다 작은 층은 쌓아야 함. 소요 시간 1초
    # 부족한 개수 : i-j
    # i-j만큼 부족한 층의 수 : floors[j]
    for j in range(min_floor, i): 
        cost += (i-j)*floors[j]
    # i보다 큰 층은 빼야 함. 소요 시간 2초
    # 뺄 개수 : j-i
    # j-i만큼 부족한 층의 수 : floors[j]
    for j in range(i, max_floor2+1):
        cost += 2*(j-i)*floors[j]
    
    # 비용 비교
    # 최저 비용이 같으면
    if cost == min_cost:
        result.append(i)
    elif cost < min_cost: # 적으면
        result = [i]
        min_cost = cost
 
print(min_cost, result[-1])