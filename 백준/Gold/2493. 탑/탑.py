N = int(input()) # 수
heis = list(map(int, input().split()))
stack = [0]*N # 높이 값
stack1 = [0]*N # stack에 대응되는 높이의 탑의 위치
result = [0]*N # 신호를 수신하는 탑 목록
top = -1 
for i in range(N-1, -1, -1): # 뒤에서부터 진행
    if top == -1: # 비어 있으면
        top += 1
        stack[top] = heis[i] # 높이 저장
        stack1[top] = i # 위치 저장
    else: # 비어 있지 않으면
        if stack[top] >= heis[i]: # 작거나 같은 애면
            top += 1
            stack[top] = heis[i] # 높이 저장
            stack1[top] = i # 위치 저장
        else: # 큰 애면
            # 지금 위치의 탑이 신호를 받을 수 있는 위치의 뒤 방향 탑들에 대해
            # (더 이상 신호를 쏜 탑이 없을 경우에도 종료)
            while stack[top] < heis[i] and top >= 0: 
                result[stack1[top]] = i+1 # 지금 탑이 신호를 받았음을 표시
                top -= 1 # 다음 탑
            # 지금 위치의 탑의 높이와 위치 저장
            top += 1 
            stack[top] = heis[i]
            stack1[top] = i

print(*result) # 결과 출력