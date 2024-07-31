# 13417. 카드 문자열

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())                # 문자의 수
  alphas = list(input().split())  # 문자 목록
  results = [alphas[0]]           # 결과
  for i in range(1, N):
    # 가장 앞 문자보다 사전순으로 앞서거나 같다면 앞으로
    if ord(alphas[i]) <= ord(results[0]):
      results.insert(0, alphas[i])
    # 그 외에는 뒤로
    else:
      results.append(alphas[i])
  
  print(''.join(results))