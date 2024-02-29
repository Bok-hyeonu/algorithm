import sys
N = int(sys.stdin.readline()) # 회의의 수
nums = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
nums.sort(key = lambda x : (x[1], x[0])) # 종료 시간을 기준으로 정렬
inge = result = 0
for num in nums: # 순회하면서
    if num[0] >= inge:  # 종료 이후 시작할 수 잇는 경우
        result += 1     # 해당 작업 
        inge = num[1]   # 종료시간 설정

sys.stdout.write(f'{result}') # 작업 회수 출력