N, K = map(int, input().split()) # N : 동전의 개수, K : 금액
stack = [0]*N # 금액을 저장할 스택
top = -1
for _ in range(N): # 스택에 각 금액을 저장
    top += 1
    stack[top] = int(input())
result = 0 # 동전의 개수
while top > -1 or K > 0: # 모든 동전 종류를 순회하며
    result += K//stack[top] # 동전을 사용할 수 있으면 사용
    K %= stack[top] # 동전 사용한 나머지
    top -= 1 # 다음 동전

print(result)