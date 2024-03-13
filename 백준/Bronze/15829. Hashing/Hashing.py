L = int(input()) # 문자열의 길이
string = input() # 입력 문자열 
total = 0
for i in range(L):
    total += (31**i)*(ord(string[i])-96) % 1234567891 # 나머지 연산 진행 후 덧셈

print(total%1234567891)