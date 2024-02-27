import sys

N = int(sys.stdin.readline())
stack = [0]*N
top = -1
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0][0] == 'p':
        if order[0][1] == 'u':
            top += 1 # push
            stack[top] = order[1]
        else: # pop
            if top == -1: sys.stdout.write('-1\n')
            else:
                sys.stdout.write(f'{stack[top]}\n')
                top -= 1
    elif order[0][0] == 't': # top
        if top == -1: sys.stdout.write('-1\n')
        else:
            sys.stdout.write(f'{stack[top]}\n')
    elif order[0][0] == 's':
        sys.stdout.write(f'{top+1}\n') # size
    else: # empty
        if top == -1: sys.stdout.write('1\n')
        else: sys.stdout.write('0\n')