def solution(n):
    trin = '' # 3진법 역수가 될 문자열
    while n >= 3: # 3보다 작아질 때까지
        trin += str(n%3) # 나머지를 문자열에 순서대로 추가
        n //= 3 # 3으로 나눈 몫을 가지고 계속 수행
    else: # 3보다 작아진 경우
        trin += str(n) # 마지막 문자열로 추가
    
    trin = trin.lstrip('0') # 0으로 시작하는 문자열의 경우 0이 아닌 수까지 0을 제거
    
    N = len(trin) # 3진법 수의 길이
    
    answer = 0 # 10진수 변환 값을 저장할 변수
    for i in range(N): # 10진법 변환
        answer += (3**(N-1-i))*int(trin[i])
    
    return answer