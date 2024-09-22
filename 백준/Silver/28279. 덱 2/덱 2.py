# 28279. 덱 2

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

deq = deque()

for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:   # front push
        deq.appendleft(order[1])
    elif order[0] == 2: # rear push
        deq.append(order[1])
    elif order[0] == 3: # front pop
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif order[0] == 4: # rear pop
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif order[0] == 5: # size
        print(len(deq))
    elif order[0] == 6: # isEmpty
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 7: # front see
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif order[0] == 8: # rear see
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])