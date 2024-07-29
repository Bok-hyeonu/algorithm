# 19941. 햄버거 분배

# 1. 햄버거를 찾는다. 전후 K만큼 사람 중 가장 앞사람에 배당한다. 
# 2. 배당한 햄버거의 수를 센 후 출력한다.

N, K = map(int, input().split())
HPs = list(input())

last_burger = -1   # 마지막으로 햄버거를 먹은 사람의 위치(인덱스)
cnt = 0             # 햄버거를 먹은 사람의 수
for i in range(N):
  # 햄버거인 경우
  if HPs[i] == 'H':
    # 전후 K만큼(단, 0, 마지막으로 햄버거를 먹은 사람의 위치 다음, 
    # 현 위치에서 K 이전 위치만큼의 
    for j in range(max(i-K, 0, last_burger+1), min(i + K + 1, N)):
      # 햄버거를 먹지 않은 첫 번째 사람이면
      if HPs[j] == 'P':
        cnt += 1  # 사람 수 증가
        last_burger = j # 마지막으로 먹은 사람의 수 증가
        break

print(cnt)