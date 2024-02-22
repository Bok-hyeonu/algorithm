N = int(input()) # 전체 숫자 수
nums = list(map(int, input().split()))
M = int(input()) # 찾아야 할 숫자 수
fnums = list(map(int, input().split()))
num_dict = dict() # 딕셔너리
for num in nums:                # 전체 숫자에 대해
    if num not in num_dict:     # 카운팅 작업 진행
        num_dict[num] = 1
    else:
        num_dict[num] += 1
for num in fnums:               # 찾고자 하는 숫자에 대해
    if num in num_dict:         # 존재하는 경우
        print(num_dict[num], end = ' ') # 해당 값을 출력
    else:                       # 없는 경우
        print(0, end = ' ')     # 0 출력