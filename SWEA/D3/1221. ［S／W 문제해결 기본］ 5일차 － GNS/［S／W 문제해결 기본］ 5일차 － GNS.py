T = int(input())
num_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9} # 값을 바꿀 딕셔너리
rev_num_dict = {val:key for key, val in num_dict.items()} # 키-값이 반대로 된 딕셔너리
for _ in range(T): # 테스트 케이스만큼 반복
    tc, N = input().split() # tc를 입력으로 받음, N : 배열의 수
    nums = list(input().split()) # 행성의 숫자 체계 수 리스트
    
    nums_list = [num_dict[num] for num in nums] # 우리 숫자 체계 변환
    nums_list.sort() # 정렬
    # 정렬된 숫자를 행성의 숫자체계로 재정렬
    result = [rev_num_dict[num] for num in nums_list]
    # 출력
    print(tc)
    print(*result)