C, R = map(int, input().split()) # C : 가로 칸 개수(열), R : 세로 칸 개수(행)
K = int(input()) # K : 대기 번호
if K > C*R: # 대기번호가 좌석수를 넘는 경우
    print(0) # 앉을 수 없음
else: # 아닌 경우
    st_x = 1 # x 위치
    st_y = 0 # y 위치
    # 개수를 맞추기 위해 1, 0에서 출발
    move = K # K회 이동
    dir = 0 # 위쪽 방향
    while move > 0: # 대기가 끝날 때까지
        if dir == 0: # 위쪽 진행 시 
            if move >= R: # 대기번호가 남은 행 수보다 크거나 같은 경우
                st_y += R # y위치 남은 행 만큼 상승
                move -= R # 대기 감소
                dir += 1 # 다음 방향(우측)
                C -= 1 # 한 열을 채웠으므로 남은 열 1 감소
            else: # 작은 경우
                st_y += move # 남은 대기만큼 위쪽으로 진행
                break # 종료
        elif dir == 1: # 우측 진행 시
            if move >= C: # 대기번호가 남은 열 수보다 크거나 같은 경우
                st_x += C # x 위치 남은 열 만큼 상승
                move -= C # 대기 감소
                dir += 1 # 다음 방향(아래)
                R -= 1 # 한 행을 채웠으므로 남은 행 1 감소
            else: # 작은 경우
                st_x += move # 남은 대기만큼 우측으로 진행
                break # 종료
        elif dir == 2: # dir 0의 경우와 유사하나 아래로 가므로 R만큼 빼줘야 함
            if move >= R:
                st_y -= R # R만큼 감소
                move -= R
                dir += 1
                C -= 1
            else:
                st_y -= move
                break
        else:
            if move >= C: # dir 1의 경우와 유사
                st_x -= C # C만큼 감소
                move -= C
                dir -= 3 # 다시 dir 0(위쪽)으로
                R -= 1
            else:
                st_x -= move
                break
    
    print(st_x, st_y) # 배정받은 좌석