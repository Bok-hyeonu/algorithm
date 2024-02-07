for tc in range(1, 11):
    N, pw = input().split()
    stack = [0] * int(N)  # 스택 저장
    top = -1
    for i in range(int(N)):
        if top == -1:  # 스택의 크기가 0이면
            top += 1  # 추가
            stack[top] = pw[i]
        else:  # 0이 아니면
            if pw[i] != stack[top]:  # 스택의 상단과 순회하는 값이 다르면
                top += 1  # 추가
                stack[top] = pw[i]
            else:  # 같으면
                stack[top] = 0  # 제거
                top -= 1
    result = ''.join(stack[:top + 1])  # 스택의 크기만큼 문자열 생성

    print(f'#{tc}', result)