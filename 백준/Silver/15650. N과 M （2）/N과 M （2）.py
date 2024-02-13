# 순열 생성 함수
def f(i, N, M): # i : 완성된 순열, N : 전체 수, M : 순열의 길이
    if i == M: # 순열 완성됐을 경우 출력
        print(*P)
    else: # 미완성인 경우
        for j in range(1, N+1): # 1부터 N까지의 수를 탐색하며 
            if i==0 or j > P[i-1]: # 첫 항이거나, 마지막 항보다 큰 경우
                P[i] = j # 해당 순열을 사용
                f(i+1, N, M) # 다음 순열로 진행

# N : 순열에 사용할 자연수 범위, M : 순열의 길이
N, M = map(int, input().split()) 
P = [0]*M # 순열의 길이만큼 빈 수열 생성
f(0, N, M) # 순열을 생성하는 함수 호출