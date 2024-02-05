for tc in range(1, 11):
    N = int(input())
    whole = ''
    for _ in range(8): # 전체 판을 하나의 문자열로 받음
        whole += input()
    
    result = 0 # 조건을 만족하는 회문의 수
    # 행(가로 방향 회문)
    for i in range(8):
        for j in range(8 - N + 1):
            string = whole[i*8 + j:i*8 + j + N] # 해당 길이 회문 슬라이싱
            for k in range(N//2): # 회문 여부 검사
                if string[k] != string[-k-1]:
                    break
            else:
                result += 1 # 회문 수 증가
    
    # 열(세로 방향 회문)
    for j in range(8):
        for i in range(8 - N + 1):
            string = whole[i*8 + j:(i + N)*8 + j:8] # 해당 길이 회문 슬라이싱
            for k in range(N//2): # 회문 여부 검사
                if string[k] != string[-k-1]:
                    break
            else:
                result += 1 # 모두 같으면 회문 수 증가
    
    print(f'#{tc}', result)