# 교집합을 찾는 연산과 동일한 방식으로 수행합니다.
import sys
N, M = map(int, sys.stdin.readline().split())
nlisten = [sys.stdin.readline().rstrip() for _ in range(N)]
nlook = [sys.stdin.readline().rstrip() for _ in range(M)]
nlisook = []
nlisten.sort()
nlook.sort()
i = 0
j = 0
while i < N and j < M:
    if nlisten[i] == nlook[j]:
        nlisook.append(nlisten[i])
        i += 1
        j += 1
    elif nlisten[i] > nlook[j]:
        j += 1
    else:
        i += 1
sys.stdout.write(f'{len(nlisook)}\n')
for nlos in nlisook:
    sys.stdout.write(f'{nlos}\n')