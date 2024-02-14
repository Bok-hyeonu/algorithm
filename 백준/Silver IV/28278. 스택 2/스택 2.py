import sys 
N = int(sys.stdin.readline())
stack = [0]*(N+1) # 스택 역할을 할 리스트
top = -1 # 포인터
for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == '1': # 정수 삽입(push)
        top += 1
        stack[top] = int(order[1])
    elif order[0] == '2': # pop
        if top == -1:
            print(top)
        else:
            print(stack[top])
            top -= 1
    elif order[0] == '3': # len
        print(top+1)
    elif order[0] == '4': # isempty
        if top == -1: print(1)
        else: print(0)
    elif order[0] == '5': # top
        if top == -1:
            print(top)
        else:
            print(stack[top])