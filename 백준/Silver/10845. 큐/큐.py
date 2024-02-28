import sys

N = int(sys.stdin.readline())
q = [0]*(N)
front = rear = -1
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0][0] == 'p':
        if order[0][1] == 'u': # push
            rear += 1
            q[rear] = order[1]
        else: # pop
            if front == rear:
                sys.stdout.write(f'-1\n')
            else:
                front += 1
                sys.stdout.write(f'{q[front]}\n')
    elif order[0][0] == 'f': # front
        if front == rear: sys.stdout.write(f'-1\n')
        else:
            sys.stdout.write(f'{q[front+1]}\n')
    elif order[0][0] == 'b': # back
        if front == rear: sys.stdout.write('-1\n')
        else:
            sys.stdout.write(f'{q[rear]}\n')
    elif order[0][0] == 'e': # empty
        if front == rear: sys.stdout.write('1\n')
        else: sys.stdout.write('0\n')
    else: # size 
        sys.stdout.write(f'{rear - front}\n')