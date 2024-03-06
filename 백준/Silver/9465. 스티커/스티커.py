import sys
# DP의 memoization 방식을 이용한다.
# 유의할 점은 직전 열의 반대 행까지의 점수 합이, 전전 열의 점수보다 낮을 수 있다.
# 따라서 비교 대상에 전전 열의 두 행도 비교 대상에 포함시킨다.
T = int(sys.stdin.readline()) # 테스트 케이스의 수
for _ in range(T):
    n = int(sys.stdin.readline()) # 스티커 쌍의 수
    sticks = [list(map(int, sys.stdin.readline().split())) for _ in range(2)] # 스티커 점수
    if n > 1: # 스티커가 1쌍보다 큰 경우
        for j in range(2):
            sticks[j][1] += sticks[(j+1)%2][0]
    # 그 다음 스티커부터는 3개의 값과 최대 최소를 비교
    for i in range(2, n):
        for j in range(2):
            # 이전 열의 반대 행이나, 전전열의 두 행 중 최댓값을 점수에 더함
            sticks[j][i] += max(sticks[(j+1)%2][i-1], sticks[0][i-2], sticks[1][i-2])
    # 마지막 열의 최댓값 출력
    sys.stdout.write(f'{max(sticks[0][-1], sticks[1][-1])}\n')