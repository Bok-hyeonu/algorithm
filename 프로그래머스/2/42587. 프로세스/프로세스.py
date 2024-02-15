# 실행 대기 큐에서 대기중인 프로세스를 하나 꺼냄
# 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금꺼낸 프로세스를 다시 큐에
# 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행
# 
def solution(priorities, location):
    N = len(priorities)
    q = [0] * (N + 1)
    front = rear = 0
    # 큐에 삽입
    for pri in priorities:
        rear += 1
        q[rear] = [pri, rear-1]
    answer = 0

    for pri in range(9, 0, -1):
        i = 0
        # 전단이 후단보다 앞인 경우와 뒤인 경우를 나누어 생각
        leng = rear - front if rear > front else rear + N + 1 - front
        while leng > i:
            i += 1
            front = (front + 1) % (N + 1)  # deque
            if q[front][0] < pri:  # 우선순위보다 작으면
                rear = (rear + 1) % (N + 1)  # enqueue
                q[rear] = q[front]
            else:  # 해당 우선순위이면
                answer += 1
                i = 0
                leng -= 1
                if q[front][1] == location:
                    return answer