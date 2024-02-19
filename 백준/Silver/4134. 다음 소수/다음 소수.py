# 소수 : 1과 자기 자신만을 약수로 하는 수
# 주어진 값 이상의 가장 작은 소수를 찾아라
import sys
T = int(sys.stdin.readline())                            # 테스트 케이스의 수
for _ in range(T):
    n = int(sys.stdin.readline())                        # 입력값
    if n <= 2:                              # 소수의 최솟값은 2
        print(2)
        continue
    if n % 2 == 0:                          # n이 4 이상의 짝수이면 
        n += 1                              # 그보다 큰 홀수부터 탐색
    while True:
        for i in range(3, int(n**0.5)+1):   # 루트 n 범위까지 탐색
            if n%i == 0:                    # 나눠지면 합성수
                break
        else:                               # 정상적으로 for문이 모두 실행된 경우 -> 소수
            print(n)          
            break
        n += 2                              # 짝수는 합성수로 탐색하지 않음