import sys
# 에라토스테네스의 체 방법을 이용하는 방법
def prime_list(n):
    n *= 2
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False
    
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    # n보다 크고, 2n보다 작거나 같은 소수의 개수
    sys.stdout.write(f'{sum(sieve[n//2+1:n+1])}\n')

while True:            
    N = int(sys.stdin.readline())
    if N == 0:
        break
    else:
        prime_list(N)