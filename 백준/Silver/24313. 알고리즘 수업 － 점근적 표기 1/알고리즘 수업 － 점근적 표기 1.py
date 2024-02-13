a1, a0 = map(int, input().split()) # a1, a0
c = int(input()) # c
n0 = int(input()) # n0
if c == a1: # 계수가 같아 상수항만 남는다면
    result = 1 if 0 >= a0 else 0 # a0가 0보다 작거나 같을 경우 참
elif c > a1: # c가 더 큰 경우
    result = 1 if n0 >= a0/(c-a1) else 0 
elif c < a1: # a1이 더 큰 경우
    result = 0 # a0에 관계없이 n이 무한히 커지면 불만족한다.
print(result)