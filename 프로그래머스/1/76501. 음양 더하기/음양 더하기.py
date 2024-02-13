def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i]: # 부호가 참이면
            answer += absolutes[i] # 더하고
        else: # 거짓이면
            answer -= absolutes[i] # 뺀다
            
    return answer