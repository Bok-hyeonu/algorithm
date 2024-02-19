# 대칭 차집합 원소의 수 = 두 집합의 원소의 수 합 - 2*교집합 원소의 수
N, M = map(int, input().split()) # N : A의 원소의 수, M : B의 원소의 수
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort() # 정렬
B.sort() # 정렬
i = j = 0
cnt = 0 # 교집합 원소의 수
while i < N and j < M:
    # 두 수의 원소가 같으면
    if A[i] == B[j]:
        cnt += 1 # 교집합 원소의 수 증가
        i += 1 # 두 집합 모두 인덱스 증가
        j += 1
    # 다르면 작은 집합의 인덱스만 증가
    elif A[i] > B[j]: 
        j += 1
    elif A[i] < B[j]:
        i += 1

print(N + M - cnt*2) # 결과 출력