for tc in range(1, 11):
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    result = 0
    for i in range(N): # 세로
        magnets = []
        for j in range(N): # 가로
            if board[j][i] != '0':
                # 하나의 세로줄에서 자석만 뽑아 교착상태 여부를 판정
                magnets.append(board[j][i])
        # 하나의 교착상태는 '12'를 포함해야만 함. 해당 수를 카운트
        result += ''.join(magnets).count('12') 
    
    print(f'#{tc}', result)      