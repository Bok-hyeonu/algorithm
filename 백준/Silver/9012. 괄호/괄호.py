# 9012 / S4 / 괄호 
T = int(input()) # 테스트 케이스의 수
for i in range(T):
    open_list = [] # 괄호를 보관할 리스트
    string = input() # 괄호 문자열
    for j in range(len(string)): # 문자열을 순회하며 
        if string[j] == '(': # 좌측 괄호일 경우
            open_list.append(string[j]) # 리스트에 추가
        else: # 우측 괄호일 경우
            if len(open_list) == 0: # 보관된 좌측 괄호가 없으면
                print('NO') # 짝이 맞지 않음 VPS 아님
                break # 반복 종료
            else:
                open_list.pop() # 보관된 좌측 괄호 1개 제거(짝)
    else: # 정상적으로 문자열을 순회한 후
        if len(open_list) == 0: # 좌측 괄호가 남아 있지 않으면
            print('YES') # VPS
        else: # 남아 있으면
            print('NO') # VPS 아님