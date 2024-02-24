import sys
N = int(sys.stdin.readline()) # 명령의 수
q = [0]*(N+1)
front = rear = -1
for _ in range(N):
    orders = list(sys.stdin.readline().split())
    if len(orders)==2: # 정수 x를 큐에 넣는 연산
        rear += 1
        q[rear] = orders[1]
    else:
        # 큐에서 가장 앞에 있는 정수를 빼고 그 수를 출력. 정수가 없으면 -1을 출력
        if orders[0][0] == 'p':
            if front == rear: sys.stdout.write('-1\n')
            else:
                front += 1
                sys.stdout.write(f'{q[front]}\n')
        elif orders[0][0] == 's': # 큐에 든 정수의 개수를 출력
            sys.stdout.write(f'{rear-front}\n')
        elif orders[0][0] == 'e': # 비어 있으면 1, 아니면 0
            if rear == front: sys.stdout.write('1\n')
            else: sys.stdout.write('0\n')
        elif orders[0][0] == 'f': # 큐의 전단에 들어 있는 정수 출력
            if front == rear: sys.stdout.write('-1\n')
            else:
                sys.stdout.write(f'{q[front+1]}\n')
        else: # 큐의 후단에 들어있는 정수 출력
            if front == rear: sys.stdout.write('-1\n')
            else:
                sys.stdout.write(f'{q[rear]}\n')