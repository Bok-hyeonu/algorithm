# 12904 A와 B
# 1. T의 과거가 S일 수 있는지 확인
# 2. S의 길이와 T의 길이가 같아질 때까지 T의 이전 상태를 한 단계씩 확인.
# 3. T의 마지막 글자가 A라면, 이전 상태에서 A를 추가했다는 것
# 3. B라면, 이전 상태에서 문자열을 뒤집고 B를 추가했다는 것
# 4. 따라서, T의 마지막 글자가 A라면, 마지막 글자(A)를 제거
# 4. B라면, B를 제거하고 문자열을 뒤집음
S = input()     # 시작 문자열
T = input()     # 목표 문자열

while len(S) != len(T): # T의 문자열이 S의 문자열의 길이와 같아질 때까지
    if T[-1] == 'A':    # T의 뒷 글자가 A라면
        T = T[:-1]      # 뒷 글자만 제거
    else:               # B라면
        T = T[:-1][::-1] # 뒷 글자를 제거하고 문자열을 뒤집음

if T == S:              # T와 S가 일치하는지 확인
    print(1)
else:
    print(0)