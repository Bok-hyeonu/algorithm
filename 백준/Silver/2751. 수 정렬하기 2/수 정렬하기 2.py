import sys
N = int(sys.stdin.readline()) # N개의 수
# N개의 수를 순서대로 입력받아 리스트에 추가
nums = [int(sys.stdin.readline()) for _ in range(N)] 
nums.sort() # 오름차순 정렬
for i in range(N): # N개의 수 순서대로 출력
    print(nums[i])
