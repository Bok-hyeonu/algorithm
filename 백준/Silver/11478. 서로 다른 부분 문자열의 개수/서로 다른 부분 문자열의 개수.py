string = input() # 문자열
result = 0
for i in range(1, len(string)+1): # 문자열 길이 지정
    subs = set()
    for j in range(len(string)-i+1): # 문자열 슬라이싱
        subs.add(string[j:j+i])
    result += len(subs) # 해당 길이의 부분 문자열 개수 추가

print(result) # 길이 출력