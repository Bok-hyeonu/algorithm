def solution(money):
    
    dp=[0]*(len(money)-1)                   # 마지막 집을 안 터는 경우
    dp[0]=money[0]                          # 집이 하나면 무조건 턴다
    dp[1]=max(money[1],money[0])            # 집이 두 개면 비싼거 턴다
    dp[2]=max(money[0]+money[2],money[1])   # 집이 3개면 1, 3번 집 or 2번 집 턴다
    
    for i in range(3,len(money)-1):         # 4번째 집부터는
        dp[i]=max(dp[i-2]+money[i],dp[i-3]+money[i-1]) # 이전 집을 안 털고 지금 집 턴 경우와 안 턴 경우의 최댓값으로 갱신
    temp=dp[-1]                             # 저장
    dp=[0]*len(money)                       # 마지막 집 턴다
    dp[0]=0                                 # 첫 집 털면 안 된다
    dp[1]=money[1]                          # 두 번째 집은 일단 털어야 한다
    dp[2]=max(money[2],money[1])            # 세 번째 집과 두 번째 집 중 비싼 집 고름
    for i in range(3,len(money)):           # 네 번째 집부터
        dp[i]=max(dp[i-2]+money[i],dp[i-3]+money[i-1])  # 이전 집을 터는게 좋은지 안 좋은지 저장
    answer=max(temp,dp[-1])             # 최종적으로 결과(마지막 집을 터는지 안 터는지) 선택
    return answer