# 조가 1개인 경우의 비용 : heights[-1] - heights[0]
# 조를 나눈다는 것 = 조의 수 - 1 만큼 인접한 두 학생의 키 차이를 무시한다는 것
# 따라서 최소화된 비용은 인접한 두 학생의 키 차이가 큰 순서대로 K-1개를
# 제외한 나머지의 합을 구하는 것
import sys
N, K = map(int, sys.stdin.readline().split()) # N : 원생의 수, K : 조의 수
heights = list(map(int, sys.stdin.readline().split())) # 원생들의 키(정렬됨)
# 키 차이 계산 및 정렬
diff = [0]*(N-1) 
for i in range(N-1):
    diff[i] = heights[i+1] - heights[i]
diff.sort()
# 키 차이가 큰 순서대로 K-1개를 제외한 총 (N-1)-(K-1)의 합을 구함
sys.stdout.write(f'{sum(diff[:(N-1)-(K-1)])}')