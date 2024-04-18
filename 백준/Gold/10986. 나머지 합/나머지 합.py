# 10986 나머지 합

# 1. i번째 수부터 j번째 수까지의 합은 첫 번째 수부터 j번째 수 까지의 합에서
# 첫 번째 수부터 i-1번째 수까지의 합을 뺀 값 (S(ij) = S(j) - S(i-1))
# 2. S(ij)가 M으로 나누어 떨어지기 위해서는 S(j)와 S(i-1)을 각각 M으로 나눈
# 나머지가 같아야 함. 예를 들어 S(j)의 나머지가 2이고 S(i-1)의 나머지가 2이면
# S(j) - S(i-1)의 나머지는 0
# 3. 따라서 S(1)부터 S(N)까지를 순회하며 M으로 나눈 나머지에 해당하는 값의 인덱스의 값을
# 1 증가(S(i)를 M으로 나눈 나머지가 0인 경우 구하고자 하는 구간의 수 1 증가)
# 4. 나머지 배열을 순회하며, 구간 쌍의 개수 증가
# 나머지가 x인 S(i)의 수가 y개라 할 때 y개의 조합을 통해 만들 수 있는 
# 구간 쌍의 수는 yC2(조합 성질 이용)

import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
S = [0]*N       # 1부터 i까지의 합 배열
lefts = [0]*M   # 나머지 배열
S[0] = A[0]     # 1부터 1까지의 합은 첫 번째 원소
result = 0      # 구하고자 하는 구간의 수

# S2부터 SN 구하기
for i in range(1, N):
    S[i] = S[i-1] + A[i]

# S1부터 SN까지의 나머지 구하기
for i in range(N):
    left = S[i] % M
    # 나머지가 0이면 구간의 수 1 증가
    if left == 0:
        result += 1
    # 해당 나머지의 값 1 증가
    lefts[left] += 1

for i in range(M):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if lefts[i] > 1:
        result += (lefts[i] * (lefts[i]-1)//2)

print(result)