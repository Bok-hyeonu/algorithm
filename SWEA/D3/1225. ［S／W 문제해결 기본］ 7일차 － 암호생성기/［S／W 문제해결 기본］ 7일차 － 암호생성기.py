for _ in range(10):
    T = int(input())
    queue = [0]*9
    front = rear = 0 # 큐 공백
    nums = list(map(int, input().split()))
    for num in nums:
        rear += 1 # enqueue
        queue[rear] = num 
    minus = 1
    while True:
        front = (front+1)%9 # 하나씩 증가시켜가면서
        rear = (rear+1)%9 
        if front != 0: # 비워둔 큐가 아니면
            if queue[front] <= minus: # minus보다 작거나 같으면
                queue[front] = 0 # 0을 삽입
                break
            else: # 크면
                queue[front] -= minus # 감소
                minus = minus% 5 + 1 # 5단위 사이클
     
    print(f'#{T}', end=' ')
     
    while front != rear: # 하나씩 빼면서 출력
        front = (front+1)%9 # dequeue
        if front != 0:
            print(queue[front], end=' ')
     
    front = (front+1)%9 # dequeue        
    print(queue[front]) # 마지막 원소 0 출력