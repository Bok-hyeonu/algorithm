# 5545. 최고의 피자

N = int(input())

A, B = map(int, input().split())  # 도우의 가격 토핑의 가격
C = int(input())  # 도우의 열량 C
Ds = [int(input()) for _ in range(N)] # 토핑의 열량

# 토핑의 열량들을 정렬
Ds.sort(reverse=True)

# 가장 열량이 높은 토핑부터 계산
for i in range(N):
  # 현재 가장 열량이 높은 토핑이 
  # 1원당 열량이 현재 피자 상태보다 크다면
  if Ds[i] / B > C / A: 
    C += Ds[i]    # 토핑 추가
    A += B        # 가격 추가
  else:           # 작다면
    break         # 그 아래는 안 봐도 됨

print(int(C / A)) # 1원당 열량 출력