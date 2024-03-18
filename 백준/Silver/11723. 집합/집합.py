# 1. 20개의 비트를 이용
# 2. 각 연산에 맞게 수행
import sys
M = int(sys.stdin.readline())
s = 0b0
for _ in range(M):
    op, *e = sys.stdin.readline().split()
    if e:                                              # 인자를 받는 경우
        e = int(e[0])-1
        if op=='check': sys.stdout.write(f'{int(bool(s&(1<<e)))}\n') # 조회 연산
        elif op=='add': s |= 1<<e                      # 추가 연산   
        elif op=='remove': s &= ~(1<<e)                # 삭제 연산
        elif op=='toggle': s ^= 1<<e                   # 반전 연산(xor)
    else:                                              # 받지 않는 연산의 경우
        if op=='all': s = 0b11111111111111111111       # 전체를 1로
        elif op=='empty': s = 0b0                      # 전체를 0으로