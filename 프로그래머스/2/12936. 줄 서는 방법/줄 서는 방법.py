def solution(n, k):
    fact = [0]*(n+1)
    fact[0] = fact[1] = 1
    for i in range(2, n+1):
        fact[i] = i*fact[i-1]
    answer = []
    nums = [i for i in range(1, n+1)]
    k -= 1
    
    for i in range(n-1, -1, -1):
        answer.append(nums[k//fact[i]])
        nums.pop(k//fact[i])
        k %= fact[i]
        
    return answer