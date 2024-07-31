# 28353. 고양이 카페

N, K = map(int, input().split())
cats = list(map(int, input().split()))

cats.sort()
i = 0
j = N - 1
cnt = 0 # 행복해지는 친구의 수
while i < j:
  # 고양이 무게를 버틸 수 있으면 
  if cats[i] + cats[j] <= K:
    i += 1    # 
    j -= 1    # 인덱스 변경
    cnt += 1  # 친구 수 증가
  else:       # 못 버티면
    j -= 1    # 가장 무거운 고양이 제외
print(cnt)    # 친구 수 출력