import itertools
# 소수인지 아닌지를 판별하는 함수
def isprime(num): 
    i = 2
    while i <= num//2:
        if num % i == 0:
            return False
        i += 1
        
    return True
    
def solution(nums):
    answer = 0
    # 원소의 수가 3개인 부분집합을 구해
    for i in itertools.combinations(nums, 3):
        num = sum(i)        # 부분집합의 합이
        if isprime(num):    # 소수이면
            answer += 1     # 개수 증가

    return answer           