def solution(board, moves):
    N = len(board) # 보드의 크기
    bucket = [0] 
    answer = 0
    for num in moves: # 인형을 뽑을 줄
        for i in range(N): # 윗 줄부터 탐색
            if board[i][num-1] != 0: # 인형이 있으면
                pick = board[i][num-1] # 인형을 뽑고
                board[i][num-1] = 0 # 해당 위치 0
                
                if pick == bucket[-1]: # 뽑은 것이 바구니의 가장 최근에 뽑은 것과 같다면
                    bucket.pop() # 해당 인형을 터뜨림 
                    answer += 2 # 터뜨린 인형 수 2 증가
                else: # 같지 않으면 
                    bucket.append(pick) # 뽑은 인형을 바구니에 추가
                
                break # 다음 줄로
        
    return answer