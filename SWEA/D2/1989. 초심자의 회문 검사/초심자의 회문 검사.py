T = int(input()) 
for tc in range(1, T + 1):
    string = input() # 입력
    for i in range(len(string)//2): # 양끝부터 중앙으로 비교
        if string[i] != string[-1-i]: # 하나라도 다를 경우
            result = 0 # 회문이 아님
            break
    else: # 모두 같을 경우 회문임
        result = 1
        
    print(f'#{tc}', result)