# 1075. 나누기

N = list(input())
F = int(input())

N.pop() # 뒤에 두 자리 바꾸기
N.pop()
# 
isFind = False
answer = '00'
for i in range(10):
    for j in range(10):
        # 뒤에 두 자리수를 바꿈
        target = int(''.join(N) + str(i) + str(j))
        # 나누어 떨어지면
        if target % F == 0:
            answer = str(i) + str(j)
            isFind = True
            break
    if isFind: break

print(answer)