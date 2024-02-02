T = int(input()) # 테스트 케이스
for tc in range(1, T + 1):
    # N : 상자의 개수, Q : 변경할 횟수
    N, Q = map(int,input().split()) 
    nums = [0]*N # 상자 배열 생성
    for i in range(1, Q + 1): # 변경할 횟수 Q회 만큼 반복
        # L : 변경 시작 박스, R : 변경 종료 박스
        L, R = map(int, input().split()) 
        for j in range(L-1, R): # 주소가 0부터 이므로 L - 1부터 R - 1까지
            nums[j] = i # i번째 변경의 값 i!

    print(f'#{tc}', *nums) # 출력