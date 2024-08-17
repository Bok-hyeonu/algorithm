import sys
nums = [0]*10001

# non-self number 구하기
for n in range(1, 10001): # 1부터 10000까지의 n에 대해
  dn = n  # n과
  ns = list(map(int, str(n))) # n을 구성하는 각 자릿수를
  dn += sum(ns) # 더함
  if dn <= 10000: # dn이 10000 이하인 경우에만 표시
    nums[dn] = 1

for i in range(1, 10001): # 1부터 10000까지의 수에 대해
  if nums[i]: # 생성자가 존재하면 pass
    continue
  sys.stdout.write(f'{i}\n')    # 존재하지 않으면 출력