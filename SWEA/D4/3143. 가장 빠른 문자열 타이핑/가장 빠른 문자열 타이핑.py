T = int(input())
for tc in range(1, T + 1):
    A, B = input().split() # A, B
    N = len(A) # A의 길이
    M = len(B) # B의 길이
    cnt = 0 # 타이핑 수
    idx = 0 # 탐색 위치
    while idx < N: # A를 순회하며
        if A[idx:idx+M] == B: # 해당 문자열이 B와 같으면
            cnt += 1 # 타이핑 수 증가
            idx += M # 다음 탐색 위치로 이동
        else: # 아니면
            idx += 1 # 다음 글자로 이동
            cnt += 1 # 타이핑 수 증가

    print(f'#{tc}', cnt) # 출력
