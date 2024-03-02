icp = {'(': 3, '*' : 2, '/' : 2, '+' : 1, '-' : 1 } # 스택 밖의 우선순위
isp = {'(': 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1 } # 스택 안의 우선순위

pf = '' # 후위 표기식
infix = input() # 입력으로 들어올 중위 표기식
stack = [0]*(len(infix)+1)
top = -1
# 입력받은 중위 표기식에서 토큰을 읽는다.
for token in infix:
    # 토큰이 피연산자이면 토큰을 출력한다.
    if ord(token) >= 65: # 아스키 코드 이용
        pf += token
    # 연산자인 경우
    else:
        # 스택 상단에 원소가 없으면 push
        if top == -1:
            top += 1
            stack[top] = token
        # 원소가 있으면
        else:
            # 토큰이 오른쪽 괄호이면 왼쪽 괄호가 올 때까지 스택에 pop 연산을 수행
            if token == ')': 
                while True:
                    t = stack[top]
                    top -= 1 
                    if t == '(':
                        break
                    else:
                        pf += t
            # 오른쪽 괄호가 아닌 다른 연산자인 경우
            else:
                # 스택이 비었으면 스택에 push
                if top == -1:
                    top += 1
                    stack[top] = token
                else:
                    # 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면,
                    # 스택에 push하고
                    if icp[token] > isp[stack[top]]:
                        top += 1
                        stack[top] = token
                    # 그렇지 않다면 토큰의 우선순위가top의 연산자의 우선순위보다 
                    # 작을 때까지 pop한 후 토큰의 연산자를 push한다. 
                    else:
                        while top != -1 and icp[token] <= isp[stack[top]]:
                            pf += stack[top]
                            top -= 1 # pop
                        top += 1
                        stack[top] = token
# 모든 중위표기식을 순회한 후 스택에 남은 연산자 pop
while top != -1:
    pf += stack[top]
    top -= 1
print(pf)