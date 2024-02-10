N = int(input()) # 약수의 개수
nums = list(map(int, input().split())) # 약수 리스트
nums.sort() # 정렬
if N%2==1: # 약수의 수가 홀수인 경우
    print(nums[N//2]**2) # (N//2+1)번째 약수의 제곱이 해당 수(인덱스므로 -1)
else: # 짝수인 경우
    print(nums[N//2-1]*nums[N//2]) # N//2, N//2+1번째 약수의 곱이 해당 수(인덱스므로 -1)