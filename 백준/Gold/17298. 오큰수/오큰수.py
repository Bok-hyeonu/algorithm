# 백준 17298. 오큰수

# 수열의 크기 N 입력
N = int(input())
# 수열 A 입력
A = [int(x) for x in input().split()]
NGE = [-1] * N

stack = [0]

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

print(*NGE)

