def solution(price, money, count):
    total = price * sum(range(1, count+1))  # 총 탑승에 필요한 금액
    if total > money:                       # 해당 금액이 가진 돈보다 큰 경우
        return total - money                # 차액 만큼 반환
    else:                                   # 가진 돈이 같거나 큰 경우
        return 0                            # 0 반환