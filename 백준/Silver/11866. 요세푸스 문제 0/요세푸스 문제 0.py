import sys

N, K = map(int, sys.stdin.readline().split()) 
nums = [i for i in range(1, N + 1)] # 수열 생성
i = -1
cnt = 0
sys.stdout.write('<')
while len(nums) != 1: # 남은 수열의 길이가 1이 될 때까지 연산 수행
    i = (i+1)%len(nums)    
    cnt += 1
    if cnt == K:
        sys.stdout.write(f'{nums[i]}, ')
        nums.pop(i)
        i -= 1
        cnt = 0
        
sys.stdout.write(f'{nums[-1]}>') # 마지막 원소 출력