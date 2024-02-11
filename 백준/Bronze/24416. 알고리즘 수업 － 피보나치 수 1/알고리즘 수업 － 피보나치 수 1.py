n = int(input()) # n의 피보나치 수 구하기
# 출력 : 재귀 실행 횟수, 동적 프로그래밍 실행 횟수
# 재귀 실행 횟수는 곧 재귀 함수의 피보나치 수
# 동적 프로그래밍 실행 횟수는 n>2인 경우, n-2(f(1)과 f(2)가 정의되므로)
def fibo(n):
    f = [0]*n
    f[0] = f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1]+f[i-2]
    return f[n-1]

print(fibo(n), n-2)