# 1966 프린터 큐
T = int(input())
for tc in range(T):
    N, M = map(int,input().split()) # N : 문서의 개수, M : 문서의 위치
    imps = list(map(int, input().split()))      # 문서들의 중요도
    imps = [(i, j) for i, j in enumerate(imps)] # 중요도와 최초 위치를 저장
    cnt = 0 # 몇 번째 순서인지를 나타내는 변수
    while True:
        # 중요도 최댓값 구하기
        max_val = imps[0][1]
        for row in imps:
            if row[1] > max_val:
                max_val = row[1]
        
        # 중요도 최댓값인 경우 출력
        # 최댓값보다 작은 경우 가장 뒤에 재배치
        while True:
            t = imps.pop(0)
            if t[1] == max_val:
                cnt += 1
                break
            else:
                imps.append(t)
        # 몇 번째 출력되는지 궁금해 하는 문서를 찾은 경우 탐색 종료
        if t[0] == M:
            break
            
    print(cnt)