import sys
# 로프가 견딜 수 있는 하중을 오름차순 정렬
# i+1번째로 큰 로프에 최대 하중이 걸리면, 해당 로프를 포함한 N-i개의 로프가 그 하중을 견딜 수 있음

N = int(sys.stdin.readline())                           # 로프의 수
ropes = [int(sys.stdin.readline()) for _ in range(N)]   # 로프가 견딜 수 있는 하중
ropes.sort()
max_weight = 0                                          # 로프들을 이용해 들어올릴 수 있는 최대 중량
for i in range(N):
    weight = ropes[i]*(N-i)
    if weight > max_weight:
        max_weight = weight
sys.stdout.write(f'{max_weight}\n')