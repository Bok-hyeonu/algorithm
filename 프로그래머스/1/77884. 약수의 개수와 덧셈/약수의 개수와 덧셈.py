# 해당하는 수가 어떤 자연수 k의 제곱이면 약수의 수가 홀수 이고,
# 아니면 약수의 수가 짝수이다. 제곱수를 제외하고는
# 어떤 수 n의 약수는 곱해서 n이 되기위한 또다른 약수가 존재한다.
def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        # 어떤 자연수의 제곱이면
        if int(num**0.5)**2==num:
            answer -= num # 빼고
        else: # 아니면
            answer += num # 더한다.
    return answer