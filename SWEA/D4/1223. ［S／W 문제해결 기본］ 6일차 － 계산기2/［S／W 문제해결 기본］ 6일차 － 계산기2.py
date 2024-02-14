def make_postfix(fx, N):
    icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖에서의 우선순위
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서의 우선순위
    top = -1
    stack = [0] * (N+1)
    postfix = ''
    for tk in fx:
        # 여는 괄호 push, 연산자이고 top 원소보다 우선순위가 높으면 push
        if top == -1 and tk in '(*+/-':
            top += 1
            stack[top] = tk
        elif tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
            top += 1 # push
            stack[top] = tk
        # 연산자이고 top 원소보다 우선순위가 높지 않으면
        elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:
            # top 원소의 우선순위가 낮을 때까지 pop
            while top != -1 and isp[stack[top]] >= icp[tk]:
                postfix += stack[top]
                top -= 1 # pop
            top += 1 # push
            stack[top] = tk
        elif tk ==')' : # 닫는 괄호면, 여는 괄호를 만날때까지 pop
            while stack[top] != '(':
                postfix += stack[top]
                top -= 1 # pop
            top -= 1 # 여는 괄호 pop 해서 버림
        else: # 피연산자인 경우 
            postfix += tk
    else: # 남은 연산자들을 순서대로 출력
        while top != -1:
            postfix += stack[top]
            top -= 1 # pop
    
    return postfix
    
for tc in range(1, 11):
    N = int(input())
    postfix = make_postfix(input(), N)
    st = [0] * (N+1)
    t = -1
    for tk in postfix:
        if tk in '+-*/': # pop 해서 연산
            if tk == '+': 
                cal = st[t-1] + st[t]
            elif tk == '-':
                cal = st[t-1] - st[t]
            elif tk == '*':
                cal = st[t-1] * st[t]
            else:
                cal = st[t-1] / st[t]
            t -= 1
            st[t] = cal # push
        else:
            t += 1 # push
            st[t] = int(tk)
        
            
    print(f'#{tc}', st[t])