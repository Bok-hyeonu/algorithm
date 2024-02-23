string = input() # 문자열
result = []
for i in range(1, len(string)+1): # 문자열 길이 지정
    for j in range(len(string)-i+1): # 문자열 슬라이싱
        result.append(string[j:j+i])

print(len(set(result))) # 길이 출력