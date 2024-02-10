def findgcd(num1, num2): # 최대공약수를 찾는 함수
    N = num1
    if num2%N==0:
        return N
    else:
        N //= 2
        while N>=1:
            if num2%N==0 and num1%N==0:
                break
            else:
                N -= 1
        return N

T = int(input()) # 테스트 케이스
for i in range(T):
    A, B = map(int, input().split())
    if A > B:
        A, B = B, A
    G = findgcd(A, B)
    print(A*B//G) # 최소 공배수는 두 수의 곱 / 두 수의 최대공약수
    