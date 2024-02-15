# 조건에 맞춰 트럭을 다리에 올린다.
# 각 트럭은 시간 1에 거리 1만큼 진행 가능하다.
# 올릴 수 있는 하중이 정해져 있다.

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 소요 시간
    q = [0] * (bridge_length + 1) # 다리 역할을 하는 큐
    front = rear = now_wei = 0
    idx = 0
    leng = 0
    
    while idx < len(truck_weights): # 트럭을 모두 다리에 올릴 때까지
        # 다리의 길이가 꽉 찬 경우
        if leng == bridge_length:
            front = (front + 1) % (bridge_length + 1)
            now_wei -= q[front][0]  # 무게만큼 빼 줌
            leng -= 1
            answer += 1
            # 다음 차량을 견딜 수 있는 경우
            if weight - now_wei >= truck_weights[idx]:
                rear = (rear + 1) % (bridge_length + 1)
                q[rear] = [truck_weights[idx], answer]
                now_wei += q[rear][0]
                leng += 1
                idx += 1
        # 꽉차지 않고 무게가 다 찬 경우
        # 가장 먼저 들어온 차가 빠져나갈 때까지 기다림
        elif weight - now_wei < truck_weights[idx]:
            front = (front + 1) % (bridge_length + 1)
            now_wei -= q[front][0]  # 무게만큼 빼 줌
            leng -= 1
            answer = q[front][1] + bridge_length  # 이동시간만큼 증가
            if weight - now_wei >= truck_weights[idx]:
                rear = (rear + 1) % (bridge_length + 1)
                q[rear] = [truck_weights[idx], answer]
                now_wei += q[rear][0]
                leng += 1
                idx += 1
        # 무게가 다 차지 않은 경우
        else:
            # 큐에 원소가 있으면서 큐 전단이 빠져 나오는 경우
            if leng != 0 and q[(front + 1) % (bridge_length + 1)][1] + bridge_length - 1 == answer:
                front = (front + 1) % (bridge_length + 1)
                now_wei -= q[front][0]  # 무게만큼 빼 줌
                leng -= 1
            rear = (rear + 1) % (bridge_length + 1)
            answer += 1
            q[rear] = [truck_weights[idx], answer]  # 무게와 진입시각을 큐에 넣음
            now_wei += q[rear][0]
            leng += 1
            idx += 1
    
    # 가장 마지막에 올린 트럭의 진입 시각에서
    # 통과에 필요한 시간을 더한다.
    answer = q[rear][1] + bridge_length

    return answer