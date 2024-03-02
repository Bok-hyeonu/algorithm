import sys
# 순열 생성 함수
def f(i, M): # i : 완성된 순열, N : 전체 수, M : 순열의 길이
    if i == M: # 순열 완성됐을 경우 출력
        sys.stdout.write(' '.join(map(str, P)) + '\n')
    else: # 미완성인 경우
        for j in range(N):
            # 사용하지 않은 수인 경우
            if visited[j] == 0:
                visited[j] = 1  # 사용을 표시 
                P[i] = nums[j]  # 해당 수를 이용
                f(i+1, M)       # 다음 수 선택
                visited[j] = 0  # 사용 여부 초기화

# N : 수열의 길이, M : 순열의 길이
N, M = map(int, sys.stdin.readline().split()) 
nums = list(map(int, sys.stdin.readline().split())) # 사용할 수열
nums.sort() 
P = [0]*M # 순열의 길이만큼 빈 수열 생성
visited = [0]*N # 수열에 사용했는지 여부를 판단하기 위한 리스트
f(0, M) # 순열을 생성하는 함수 호출