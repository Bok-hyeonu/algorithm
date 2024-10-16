# 9613. GCD 합

import sys
input = sys.stdin.readline

# while문을 활용한 유클리드 호제법 구현
def get_gcd(a, b): 
	while b : 
		a, b = b, a % b
	return a

t = int(input())
for _ in range(t):
    n, *nums = map(int, input().split())
    total = 0
    # 각 쌍에 대해 gcd를 구해 더함
    for i in range(n - 1):
        for j in range(i + 1, n):
            total += get_gcd(nums[i], nums[j])
    
    print(total)