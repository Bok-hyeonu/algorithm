def solution(new_id):
    new_id = new_id.lower() # 1단계(소문자 치환)
    answer = ''
    for i in range(len(new_id)): # 2단계(알파벳, 숫자, -_. 제외 제거)
        if new_id[i].isalpha() or new_id[i].isdecimal(): # 영어 소문자나 숫자면
            answer += new_id[i]
        else:
            if new_id[i] in '-_.':
                answer += new_id[i]
    idx = len(answer)-1 # 3단계(연속되는 . 제거하기)
    while idx >= 1: 
        if answer[idx] == '.':
            if answer[idx-1] == '.':
                answer = answer[:idx-1] + answer[idx:]
        idx -= 1
    answer = answer.strip('.') # 4단계(마침표가 처음이나 끝에 위치한다면 제거하기)
    if len(answer) == 0: # 5단계(문자열이 비었다면 a 대입)
        answer = 'a' 
    elif len(answer) >= 16: # 6단계(16자 이상인 경우 첫 15자까지)
        answer = answer[:15]
        answer = answer.rstrip('.')
    
    if len(answer) <= 2: # 7단계(2자 이하면, 3자가 될 때까지 마지막 글자)
        while len(answer) <= 2:
            answer = answer + answer[-1]    
    
    return answer