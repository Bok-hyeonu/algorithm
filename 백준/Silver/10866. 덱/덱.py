import sys

N = int(sys.stdin.readline())
d = [0]*(N+1) # 덱
front = rear = 0

# 덱의 크기를 충분히 주었으므로 삽입 연산에서의 포화 상태는 검사하지 않는다.
for _ in range(N):
    order = list(sys.stdin.readline().split()) # 명령
    if order[0] == 'push_back': # 후단 삽입
        rear = (rear+1)%(N+1) # 후단 원소를 증가 시킨 후
        d[rear] = order[1]  # 삽입
    elif order[0] == 'push_front': # 전단 삽입
        d[front] = order[1] # 삽입하고
        front = (front-1)%(N+1) # 전단 원소 감소
    elif order[0] == 'pop_front': # 전단 삭제
        # 공백인 경우
        if rear == front: sys.stdout.write('-1\n')
        # 공백이 아닌 경우
        else:
            front = (front+1)%(N+1)
            sys.stdout.write(f'{d[front]}\n')     
    elif order[0] == 'pop_back': # 후단 삭제
        # 공백인 경우
        if rear == front: sys.stdout.write('-1\n')
        # 공백이 아닌 경우
        else:
            sys.stdout.write(f'{d[rear]}\n')
            rear = (rear-1)%(N+1)
    elif order[0] == 'size': # 원소의 수
        if rear >= front: sys.stdout.write(f'{rear-front}\n')
        else:
            sys.stdout.write(f'{rear+N+1-front}\n')
    elif order[0] == 'empty' : # 공백 덱 여부
        if rear == front: sys.stdout.write('1\n')
        else: sys.stdout.write('0\n')
    elif order[0] == 'front': # 전단 원소
        # 공백인 경우
        if rear == front: sys.stdout.write('-1\n')
        # 공백이 아닌 경우
        else:
            sys.stdout.write(f'{d[(front+1)%(N+1)]}\n')
    else: # 후단 원소
        # 공백인 경우
        if rear == front: sys.stdout.write('-1\n')
        # 공백이 아닌 경우
        else:
            sys.stdout.write(f'{d[rear]}\n')