N = int(input()) # 수열의 길이
nums = list(map(int, input().split()))
max_c = plus_cnt = minus_cnt = 0 # 카운팅 변수(최대, 증가, 감소)
pos_v = nums[0] 
for num in nums: 
    if num == pos_v: # 이전 값과 같으면
        plus_cnt += 1 # 증감 방향 모두 카운팅 증가
        minus_cnt += 1 
    elif num > pos_v: # 증가 방향이면
        plus_cnt += 1 # 증가 방향 증가
        minus_cnt = 1 # 감소 방향 초기화
    elif num < pos_v: # 감소 방향이면
        minus_cnt += 1 # 감소 방향 증가 
        plus_cnt = 1 # 증가 방향 초기화
    
    if plus_cnt > max_c: # 어느 하나라도 최대 연속보다 크면
        max_c = plus_cnt 
    elif minus_cnt > max_c: # 해당 값으로 최대 연속 변경
        max_c = minus_cnt
    
    pos_v = num # 다음 탐색 값

print(max_c) # 출력
        