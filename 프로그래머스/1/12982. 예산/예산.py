# sort 사용
def solution(d, budget):
    answer = 0                  # 지원 부서의 수
    d.sort()                    # 신청금액 적은 순으로 나열, 가장 많은 부서에 지원하기 위함
    for bud in d:               # 신청금액이 적은 순서대로 
        if budget >= bud:       # 신청금액 합이 예산을 넘지 않는 범위이면    
            budget -= bud       # 예산 사용
            answer += 1         # 지원 부서 1 증가
        else:                   # 신청금액 합이 예산을 넘게 되면
            break               # 지금까지의 부서만 지원
    return answer