# 2343. 기타 레슨

# 1. 블루레이의 최소 크기는 각 강의 길이의 최댓값, 최대 크기는 전체 합
# 2. 블루레이의 크기별 이진 탐색을 수행
# 3. 최종 start의 값이 디스크 크기의 최솟값

N, M = map(int, input().split())  # 레슨 수, 블루레이 수
lessons = list(map(int, input().split())) # 각 강의의 길이 수

start = max(lessons)    # 블루레이 크기의 최소
end = sum(lessons)      # 최대

while start <= end:     # 하한이 상한을 넘기 전까지
    middle = int((start + end) // 2)    # 중간값을 디스크의 크기로
    total = 0       # 합
    cnt = 1         # 필요한 블루레이의 개수(최소 1)
    for i in range(N):
        # 디스크 크기를 넘어서면 블루레이 개수와 용량 합 최소화
        if total + lessons[i] > middle:
            cnt += 1
            total = 0
        # 넘어서지 않았다면 계속 할당
        total += lessons[i]
    # 블루레이 수가 보유한 수보다 많으면
    if cnt > M:
        # 하한을 조정
        start = middle + 1
    # 이하이면 상한을 조정
    else:
        end = middle - 1
        
print(start)