# 6603 로또
# 1. 조합 문제 주어진 수에서 6개의 숫자를 오름차순으로 뽑아내면 된다.
# 2. 예를 들어, 8개의 수가 주어진 경우, 6개의 번호 중 3번째 번호에는
# 8개의 수 중 5번째 숫자까지 올 수 있다. 뒤에 최소 빈 숫자의 수만큼은 남겨야 함
import sys
def f(i, jj):
    # 6개의 숫자가 모인 경우 출력 
    if i == 6:
        sys.stdout.write(f'{" ".join(map(str, P))}\n')
        return
    # 시작 인덱스(이전 입력보단 커야 함), 종료 인덱스(입력으로 주어진 수에 따라 해당 순번에서의 최대 인덱스가 제한)
    for j in range(max(i, jj+1), inputs[0]-5+i):
        P[i] = inputs[j+1]
        f(i+1, j)
    return

while True:
    # 입력
    inputs = list(map(int, input().split()))
    # 0인 경우 종료
    if inputs[0]:
        P = [0]*6
        f(0, -1)
        sys.stdout.write('\n')  # 테스트 케이스 간 빈 줄
    else:
        break