n = int(input()) # 피보나치 수와 같음
memo = [1]*(n+1)
if n>=2: # 피보나치 수 계산
    for i in range(2, n+1):
        memo[i] = (memo[i-1] + memo[i-2])%15746 
        # 미리나눠주지 않으면 메모리 과부하
        
print(memo[n])