# 10799. 쇠막대기

# 1. 레이저 포인터인지 막대인지를 구분
# 2. 레이저 포인터라면 쌓인 막대의 수를 조각의 수로 더함
# 3. 레이저 포인터가 아닌 막대라면 막대의 수를 쌓음
# 4. 막대의 마지막이라면 마지막 한 조각을 더함

# 막대기 입력
bars = list(input())

# 현재까지 쌓인 막대의 수
bar = 0

# 잘린 막대 조각의 수
barpieces = 0

# 각 지점을 탐색하며
for i in range(len(bars)):
    # 여는 괄호일 때
    if bars[i] == '(':
        # 다음 괄호가 닫는 괄호이면(레이저 포인터라면)
        if bars[i + 1] == ')':
            barpieces += bar    # 쌓인 막대 수만큼 조각내서 더함
        # 닫는 괄호가 아니면(막대를 의미한다면)
        else:
            bar += 1    # 쌓인 막대 수 + 1
    # 닫는 괄호일 때
    else:
        # 이전 괄호가 닫는 괄호이면(이 지점이 어느 막대의 마지막을 의미하면)
        if bars[i - 1] == ')':
            # 쌓인 막대의 수 - 1
            # 막대 조각의 수 + 1
            barpieces += 1
            bar -= 1

print(barpieces)