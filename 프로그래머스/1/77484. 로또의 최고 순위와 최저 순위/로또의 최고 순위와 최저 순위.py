def solution(lottos, win_nums):
    answer = []
    best = 0 # 최고
    worst = 0 # 최저
    for num in lottos:
        if num == 0: # 알 수 없는 경우
            best += 1 # 최상의 경우 맞춘 번호 증가
        elif num in win_nums: # 로또 번호 맞춘 경우
            best += 1 # 최상
            worst += 1 # 최악 모두 증가
    worst = 1 if worst == 0 else worst # 맞춘 번호 없으면 1로
    best = 1 if best == 0 else best 
    answer.append(7-best)
    answer.append(7-worst)
    
    return answer