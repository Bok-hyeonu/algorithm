# 10810 / B3 / 공 넣기
N, M = map(int, input().split()) # N : 바구니 수, M : 공을 넣는 행위의 수
bucket = [0]*N # 바구니 생성
for _ in range(M): # M회 반복
    # i : 시작 바구니, j : 종료 바구니, k : 공 번호
    i, j, k = map(int, input().split()) 
    # 시작 바구니 번호는 - 1, 종료 바구니 번호도 - 1, 따라서 i-1, j까지 탐색
    for l in range(i-1, j): 
        bucket[l] = k # 해당 바구니에 k번 공을 넣음
print(*bucket) # 출력