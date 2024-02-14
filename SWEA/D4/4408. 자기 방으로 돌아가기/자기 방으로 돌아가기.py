# 통로를 200 분할하였을 때, 학생들은 동시간대에 같은 통로를 이용할 수 없음
# 따라서 모든 학생이 방으로 돌아가기 위한 최단 단위 시간은
# 200개의 통로 중 이용횟수가 가장 많은 통로의 수와 같음

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 돌아갈 학생 수
    path = [0]*201  # 각 경로 사용횟수를 저장할 리스트
    cnt = 0
    for i in range(N):
        A, B = map(lambda x: (int(x)+1)//2, input().split())
        if A > B: # 출발지가 도착지보다 뒷 번호 방인 경우
            A, B = B, A # 순서 변경
        for i in range(A, B+1): # 해당 통로 이용했음을 표시
            path[i] += 1
    
    print(f'#{tc}', max(path)) # 최댓값