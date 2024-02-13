def make_postfix(fx, N):
    top = -1
    stack = [0] 
    postfix = ''
    for tk in fx:
        if top == -1 and tk == '+': # 첫 +인 경우
            top += 1
            stack[top] = tk
        elif tk == '+': # 아닌 경우
            postfix += tk
        else: # 피연산자인 경우 
            postfix += tk
    else:
        postfix += stack[top]
        top -= 1 # pop
    
    return postfix
    
for tc in range(1, 11):
    N = int(input())
    postfix = make_postfix(input(), N)
    st = [0] * (N+1)
    t = -1
    for tk in postfix:
        if tk == '+': # pop 해서 연산
            cal = st[t] + st[t-1]
            t -= 1
            st[t] = cal # push
        else:
            t += 1 # push
            st[t] = int(tk)
        
    print(f'#{tc}', st[t])