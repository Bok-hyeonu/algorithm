import sys
def f(lst, d):
    global res
    # 수를 찾았을 경우, 연산횟수를 비교하여 최저 연산 수 
    if lst == Bt:
        if d < res:
            res = d
            return
    # 수의 길이가 목표 수보다 긴 경우
    elif len(lst) > len(Bt):
        return
    # 아직 추가 연산이 가능한 경우 추가 연산 진행
    else:
        # 2를 곱하는 연산
        f(list(str(int(''.join(lst))<<1)), d + 1)
        # 뒤에 1을 더하는 연산
        f(lst+['1'], d+1)

A, B = sys.stdin.readline().split()
Bt = list(str(B)) # 목표
res = 31 # 이를 수 있는 최고 깊이
At = list(str(A)) # 현재
f(At, 0)
if res == 31: res = -1
else: res += 1
sys.stdout.write(f'{res}\n')