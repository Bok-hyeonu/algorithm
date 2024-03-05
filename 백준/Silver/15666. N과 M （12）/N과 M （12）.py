import sys
# i : 순열의 i번째 원소, jj : nums 중 현재 사용한 원소, k : 순열의 마지막
def f(i, jj, k): 
    if i == k:
        sys.stdout.write(f"{' '.join(map(str, P))}\n")
    else:
        for j in range(jj, N):
            P[i] = nums[j]
            f(i+1, j, k)
            

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums = list(set(nums))  # 중복 요소 제거
nums.sort()             # 오름차순 정렬
N = len(nums)
P = [0]*M
f(0, 0, M)