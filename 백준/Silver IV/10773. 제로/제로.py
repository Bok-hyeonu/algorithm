import sys
K = int(sys.stdin.readline())
top = -1 # 포인터
stack = [0]*K # 스택
for i in range(K): 
    N = int(sys.stdin.readline())
    if N == 0: # 0이면 pop
        top -= 1
    else: # 아니면 push
        top += 1
        stack[top] = N
print(sum(stack[:top+1])) # top까지의 총합