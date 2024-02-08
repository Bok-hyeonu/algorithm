T = int(input())
for tc in range(1, T + 1):
    bars = input() # 입력 막대기
    result = 0 # 잘라진 총 개수
    cnt = 0 # 쌓인 막대 수
    for i in range(len(bars)): # 막대들을 순회하며
        if bars[i]=='(': # 여는 괄호면
            cnt += 1 # 쌓인 막대 수 1 증가
        else: # 닫는 괄호면
            if bars[i-1]=='(': # 레이저를 쏜 경우라면
                cnt -= 1 # 방금 연 괄호가 레이저 였으므로 감소
                result += cnt # 지금 쌓인 막대 수만큼 개수 증가
            else: # 어떤 막대의 종료 시점이라면
                result += 1 # 해당 막대 조각만 증가
                cnt -= 1 # 쌓인 막대 수 감소
     
    print(f'#{tc}', result) # 출력