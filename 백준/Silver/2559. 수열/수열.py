N, K = map(int, input().split()) # N : 전체 측정 날짜, K : 연속 요일
temp_list = list(map(int, input().split())) # 길이 N의 온도 리스트
total = hap = sum(temp_list[:K]) # 길이 K의 온도 합
for i in range(1, N-K+1): # N-K+1일 까지
    hap -= temp_list[i-1] # 가장 오래된 날 온도 빼고
    hap += temp_list[i+K-1] # 가장 최신 온도 더하고
    if hap > total: # 기존의 최댓값보다 크다면 
        total = hap # 최댓값 변경

print(total) # 최댓값 출력
