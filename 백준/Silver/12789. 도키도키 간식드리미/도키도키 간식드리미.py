N = int(input()) # 승환이 앞 학생들의 수
students = list(map(int, input().split()))
stack = [0]*N # 빠질 수 있는 줄
top = -1
seq = 1
for i in range(N):
    # 스택에 원소가 있으면서 상단이 번호표 순서와 같은 경우
    if top != -1 and stack[top] == seq:
        while stack[top] == seq: # 번호표 순서가 같은 만큼 뽑아냄
            seq += 1
            top -= 1
    # 줄 선 곳에 맨 위의 학생이 현재 순서면
    if students[i] == seq:
        seq += 1 # 해당 학생 통과
    else: # 현재 순서가 아닌 경우 중
        # 스택에 원소가 있으면서 스택 상단보다 현재 값이 큰 경우
        if top != -1 and stack[top] < students[i]:
            result = 'Sad' # Sad 반환
            break
        else: # 아닌 경우
            top += 1 # 스택에 쌓음
            stack[top] = students[i]
else: # 정상 종료 시
    while top != -1 and stack[top]==seq: # 스택을 순서대로 빼냄
        seq += 1 
        top -= 1
    result = 'Nice' if top == -1 else 'Sad' # 다 빼냈다면 Nice, 아니면 Sad
print(result)