def sum_of_digits(n):
    # 숫자의 각 자릿수를 더하는 함수
    return sum(int(digit) for digit in str(n))

def hindu_check(equation, case_num):
    # 주어진 식에 대해 힌두 체크를 수행하는 함수
    if '+' in equation:
        # 덧셈의 경우 처리
        a, rest = equation.split('+')
        b, c = rest.split('=')
        operation = 'addition'  # 덧셈
    elif '*' in equation:
        # 곱셈의 경우 처리
        a, rest = equation.split('*')
        b, c = rest.split('=')
        operation = 'multiplication'  # 곱셈
    
    # a, b, c를 정수로 변환 (마지막에 붙은 점(.)을 제거)
    a, b, c = int(a), int(b), int(c.strip('.'))
    
    # a, b, c의 자릿수 합을 구하고 이를 9로 나눈 나머지를 구함
    a_bar = sum_of_digits(a) % 9
    b_bar = sum_of_digits(b) % 9
    c_bar = sum_of_digits(c) % 9
    
    # 덧셈 또는 곱셈에 대해 체크를 수행
    if operation == 'addition':
        if (a_bar + b_bar) % 9 == c_bar:
            return f"{case_num}. PASS"  # 조건이 맞으면 PASS
        else:
            return f"{case_num}. NOT!"  # 조건이 틀리면 NOT!
    elif operation == 'multiplication':
        if (a_bar * b_bar) % 9 == c_bar:
            return f"{case_num}. PASS"  # 조건이 맞으면 PASS
        else:
            return f"{case_num}. NOT!"  # 조건이 틀리면 NOT!

def process_hindu_checks():
    # 표준 입력을 통해 여러 줄을 입력받아 처리
    case_num = 1
    results = []
    
    while True:
        line = input().strip()  # 한 줄씩 입력받고 양쪽 공백을 제거
        if line == '.':
            break  # 입력의 끝을 나타내는 '.' 처리
        result = hindu_check(line, case_num)
        results.append(result)
        case_num += 1
    
    # 결과 출력
    for result in results:
        print(result)

# 실제 실행부
process_hindu_checks()