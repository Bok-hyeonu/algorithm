# 1026. 보물

# 1. 곱의 합이 최소가 되게 하기 위해서는 A는 오름차순으로 B는 내림차순으로 정렬된 상태로 곱해져야 한다.


N = int(input())    # 길이
A = list(map(int, input().split())) # 배열 A
B = list(map(int, input().split())) # 배열 B

A.sort()                # 배열 A는 순방향 정렬
B.sort(reverse=True)    # 배열 B는 역방향 정렬
# 계산
total = 0
for i in range(N):
    total += A[i]*B[i]

print(total)