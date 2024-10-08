N, a, b = map(int, input().split())

# 최종 라운드 세기
cnt = 0
while N > 1:
  cnt += 1
  N //= 2

# 맞대결 라운드 구하기(cnt + 1 + 1로 설정)
for i in range(1, cnt + 2):
  a = (a + 1) // 2
  b = (b + 1) // 2
  if a == b:
    break

# 결과 출력
print(i)