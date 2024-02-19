# 편의상 *, 0, #을 10, 11, 12로 간주하고 풀이한다.
def solution(numbers, hand):
    answer = ''
    pos_l = 10                      # *을 10으로
    pos_r = 12                      # #을 12로 0을 12로
    for number in numbers:          # 모든 수에 대해서
        if number in (1, 4, 7):     # 숫자가 왼쪽 수면
            answer += 'L'           # L 추가
            pos_l = number          # 왼손의 위치 변경
        elif number in (3, 6, 9):   # 오른쪽 수면
            answer += 'R'           # R 추가
            pos_r = number          # 오른손의 위치 변경
        else:                       # 가운데 수면
            ppos_r = pos_r          # 기존 위치값 이용
            ppos_l = pos_l          
            dis_r = dis_l = 0       # 거리 초기화
            if number == 0:         # 0이면 편의상 11로 간주
                number = 11         
            if ppos_r % 3 == 0:     # 현재 오른손이 오른쪽 라인에 있는 경우
                dis_r += 1          # 거리 증가(가운데 라인으로 이동)
                ppos_r -= 1         # 좌측으로 이동
            if ppos_l % 3 == 1:     # 왼쪽 라인에 있는 경우
                dis_l += 1          # 거리 증가(가운데 라인으로 이동)
                ppos_l += 1         # 우측으로 이동
            
            # 양 손 모두 차의 절댓값을 3으로 나눈 것 만큼 거리 증가
            dis_l += abs(ppos_l-number)//3  
            dis_r += abs(ppos_r-number)//3
            
            
            if dis_l == dis_r:       # 거리가 동일한 경우 주손에 따라 결정
                if hand == 'left':
                    answer += 'L'
                    pos_l = number
                else:
                    answer += 'R'
                    pos_r = number
            elif dis_l < dis_r:      # 거리가 다르다면 가까운 손으로 결정
                answer += 'L'
                pos_l = number
            else:
                answer += 'R'
                pos_r = number
                   
    return answer