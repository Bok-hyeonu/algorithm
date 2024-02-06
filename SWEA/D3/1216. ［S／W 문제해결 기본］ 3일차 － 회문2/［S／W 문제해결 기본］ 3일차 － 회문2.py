for tc in range(1, 11): 
    T = int(input()) # 테스트 케이스
    board = ''
    for _ in range(100): # 입력을 하나의 문자열로 받음
        board += input()
    
    # 가능한 최대 회문 길이부터 조사하며, 회문이 발견될 경우 그대로 종료하는 알고리즘
    result = 101 # 최대 회문의 길이
    cnt = 0 # 회문 수
    while cnt == 0: # 회문이 하나라도 발견됐을 경우 반복 종료
        result -= 1 # 최대 회문 길이 1 감소
        # 행 검사
        for i in range(100): # 행 위치
            for j in range(100 - result + 1): # 열 위치 
                string = board[i * 100 + j:i * 100 + j + result] # 문자열 슬라이싱
                for k in range(result // 2): # 회문 여부 검사
                    if string[k] != string[-k - 1]:
                        break
                else: # 회문인 경우
                    cnt += 1 
        # 열 검사
        for j in range(100): # 열 위치 
            for i in range(100 - result + 1): # 행 위치
                string = board[i * 100 + j:(i + result) * 100 + j:100] # 매 100칸(곧 열)
                for k in range(result // 2): # 회문 여부 검사
                    if string[k] != string[-k - 1]:
                        break
                else: # 회문인 경우
                    cnt += 1

    print(f'#{T}', result) # 회문이 발견된 길이 반환