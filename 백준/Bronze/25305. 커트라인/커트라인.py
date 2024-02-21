N, K = map(int, input().split())            # 총 응시자 수 K, 수상자 수 K
scores = list(map(int, input().split()))    # 점수
scores.sort()       # 오름차순 정렬
print(scores[-K])   # 오름차순 정렬에서 끝에서 K번째 수