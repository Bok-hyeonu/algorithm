def solution(a, b):
    answer = 0 
    for i in range(len(a)): # 내적을 구하는 식
        answer += a[i]*b[i]
    return answer