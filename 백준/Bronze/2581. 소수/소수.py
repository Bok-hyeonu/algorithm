def isprime(n):
    if n==1:
        return False
    div = 2
    while div**2 <= n:
        if n%div==0:
            return False
        div += 1
    else:
        return True

M = int(input())
N = int(input())
result = []
for num in range(M, N+1):
    if isprime(num):
        result.append(num)
else:
    if len(result)==0:
        print(-1)
    else:
        print(sum(result))
        print(result[0])   