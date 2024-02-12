N = int(input()) # 학생의 수
nums = list(map(int, input().split()))
result = [1]
for i in range(1, N): # 나머지 n-1명 줄 세우기
    # i : 현재 길이 - 1이자 마지막 인덱스
    # nums[i] : 맨 뒤로부터 앞으로 가야할 값
    # i + 1 : 학생의 번호
    result.insert(i-nums[i], i+1) 
    
print(*result)