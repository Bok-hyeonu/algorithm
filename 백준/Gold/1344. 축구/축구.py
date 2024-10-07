# 1344. 축구

# 1. 5분 간격으로 나누었으므로 각 팀당 득점 가능 수는 18
# 2. 1~18 사이 소수에 대해 각 팀의 해당 점수만큼 득점할 확률을 계산한다.
# 다른 풀이 : 소수 아닌 수를 득점할 확률을 구한 뒤 1에서 양 팀 모두 소수 아닌 수를 득점할 확률의 곱을 빼준다

import sys
input = sys.stdin.readline
from itertools import combinations, permutations

a = int(input())    # A팀 득점 확률
b = int(input())    # B팀 득점 확률

# 득점의 최댓값은 18
check = [2, 3, 5, 7, 11, 13, 17] # 18 이하의 소수
c = [ i for i in range(1, 19)] 

pera = a/100.0
perb = b/100.0
sa = sb = 0

# 확률 구하는 공식
# p(k) = 18Ck * P**k * (1-p)**18-k 
for i in range(len(check)):
    # nC2 조합 n!/((n-r)! * r!)
    combi = len(list(combinations(c, check[i]))) # 18Ck
    sa += combi * pow(pera, check[i]) * pow(1.0-pera, 18-check[i])
    sb += combi * pow(perb, check[i]) * pow(1.0-perb, 18-check[i])

print(sa+sb - sa*sb) # 두 팀이 동시에 소수 점수를 낼 확률을 빼주기