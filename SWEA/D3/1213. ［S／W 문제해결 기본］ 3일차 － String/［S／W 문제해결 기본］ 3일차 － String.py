for _ in range(1, 11):
    T = int(input())
    str1 = input() # 찾으려는 문자열
    str2 = input() # 주어진 문자열
    result = 0 
    str1_dict = {} # 위치값
    for i in range(1, len(str1)): # 마지막 글자를 제외하고 순회하며
        if str1[-i-1] not in str1_dict: # 해당 글자가 없으면 추가한다.
            str1_dict[str1[-i-1]] = i
    
    idx = len(str1) # 시작 인덱스는 str1의 길이
    while idx < len(str2): # str2 인덱스 내에서
        if str2[idx] == str1[-1]: # 조회하는 인덱스가 str1의 끝 글자와 같으면
            for i in range(len(str1)): # 같은지 확인
                if str2[idx-i]!=str1[-i-1]: # 하나라도 다르면
                    # 끝 글자가 문자열 안에 다른 위치에도 있으면
                    if str2[idx] in str1_dict: 
                        idx += str1_dict[str2[idx]] # 해당 위치로 이동
                    else:
                        idx += len(str1) # 없으면 글자 수만큼 이동
                    break
            else: # 같으면 개수 추가
                result += 1
                idx += len(str1) # 글자 수만큼 이동

        else: # 끝 글자와 다르면
            if str2[idx] in str1_dict:
                idx += str1_dict[str2[idx]]
            else:
                idx += len(str1)
    
    print(f'#{T}', result)