def solution(n,a,b):
    answer = 0                  # 라운드
    while a!=b:                 # 비트 연산을 계속 진행하여 값이 같아지면 해당 라운드 하나 전에서 만남
        if a % 2 == 0:          # 짝수면 다음 라운드 N/2번
            a >>= 1
        else:                   # 홀수면
            a = (a>>1) + 1      # 다음 라운드 N//2 + 1번
        if b % 2 == 0:          
            b >>= 1
        else:
            b = (b>>1) + 1
        answer += 1             # 라운드 증가
    # answer - 1을 해줘야 하나 round 시작이 0라운드였으므로 감소할 필요 X
    return answer