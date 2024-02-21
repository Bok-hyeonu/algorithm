N = int(input()) # 입력의 수
nums = list(map(int, input().split()))
numbers = [[nums[i], i, 0] for i in range(N)] # 숫자, 원래 인덱스, 압축 좌표(0)
numbers.sort()                      # 정렬(오름차순)
pre = numbers[0][0]                 # 동일한 값을 비교하기 위한 이전 값
cmp = 0                             # 압축된 좌표값
for num in numbers:                 # 정렬된 좌표들을 순회하며 압축 좌표 삽입
    if num[0] == pre:               # 같으면, 이전 좌표와 같은 좌표를 삽입
        num[2] = cmp
    else:                           # 다르면 
        cmp += 1                    # 좌표값 1 증가 후 삽입
        num[2] = cmp
        pre = num[0]                # 비교할 좌표 변경
numbers.sort(key = lambda x:x[1])   # 기존 인덱스를 키로 정렬
result = [num[2] for num in numbers]# 압축된 좌표만을 새로운 리스트로 생성
print(*result)                      # 출력