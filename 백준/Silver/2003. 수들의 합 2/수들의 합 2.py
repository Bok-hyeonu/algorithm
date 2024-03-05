import sys
# N : 수열의 길이, M : 목표 합
N, M = map(int, sys.stdin.readline().split()) 
arr = list(map(int, sys.stdin.readline().split()))
# 투 포인터
st = ed = cnt = 0
total = 0
while True:
    # 총 합이 목표보다 작은 경우
    if total < M:
        # 인덱스를 늘릴 수 없는 경우 종료
        if ed == N:
            break
        # ed가 가리키는 인덱스를 증가
        total += arr[ed]
        ed += 1 # ed의 인덱스 증가
    else:
        # 목표와 같은 경우
        if total == M:
            # 개수 상승
            cnt += 1
        # st 인덱스 값을 빼주고 1 상승
        total -= arr[st]
        st += 1
print(cnt)