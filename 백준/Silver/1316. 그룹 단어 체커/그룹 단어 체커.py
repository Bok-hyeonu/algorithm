N = int(input()) # 단어의 수
cnt = 0 # 그룹 단어의 수
for _ in range(N): # N회 반복
    word = input() # 대상 단어
    rem_list = [] # 사용된 알파벳
    ser = word[0] # 현재 알파벳
    i = 1 # 다음 위치부터 탐색 시작
    while i < len(word): # 길이만큼
        if word[i] in rem_list: # 사용된 알파벳 리스트에 있으면
            break # 반복 종료
        else: # 없으면
            if word[i] == ser: # 탐색하는 알파벳이 이어진다면
                pass 
            else: # 이어지지 않는다면
                rem_list.append(ser) # 이전 알파벳을 사용된 리스트에 추가
                ser = word[i] # 현재 알파벳 갱신
            i += 1 # 다음 위치로
    else: # 정상 동작한 경우
        cnt += 1 # 그룹 단어

print(cnt) # 출력