# 2346. 풍선

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    # 위치와 풍선 안에 적힌 종이
    idx, paper = q.popleft()
    ans.append(idx + 1)
    # 양수 음수에 따른 회전 진행
    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))