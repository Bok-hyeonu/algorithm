# memoization을 이용한 피보나치
# 피보나치에서 f(0)과 f(1)의 호출횟수 역시 피보나치 수열을 따름
# f0(0) = 1, f0(1) = 0, f1(0) = 0, f1(1) = 1을 첫 두 항으로 하는 피보나치 수열
def fibo0(n): 
    f0 = [0] * (n+1)
    f0[0] = 1
    if n > 0:
        f0[1] = 0
        for i in range(2, n+1):
            f0[i] = f0[i-1] + f0[i-2]
    
    return f0[n]

def fibo1(n):
    f1 = [0] * (n+1)
    f1[0] = 0
    if n > 0:
        f1[1] = 1
        for i in range(2, n+1):
            f1[i] = f1[i-1] + f1[i-2]
    
    return f1[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(fibo0(N), fibo1(N))