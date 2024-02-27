import sys
n = int(sys.stdin.readline())
stack = [0]*n # 스택
ans = [] # 정답 배열
res = True # 연산이 가능한지
now = 1 # push 가능한 숫자
top = -1 # 포인터
for i in range(n): # 수열에 대해
    num = int(sys.stdin.readline()) # 수열
    if res: # 이전에 계속 성공한 경우만 진행
        while now <= num: # num까지 계속 push
            top += 1
            stack[top] = now
            ans.append('+')
            now += 1
        if stack[top] == num: # 상단이 num이면
            top -= 1 # pop
            ans.append('-')
        else: # num이 아니면
            res = False # 출력 불가
if res: # 최종 연산 성공시에만 출력
    for a in ans: # 연산자 출력
        sys.stdout.write(f'{a}\n')
else: # 실패 시 NO 출력
    sys.stdout.write(f'NO\n')