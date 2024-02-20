# 입력받은 수의 포화이진트리 형태의 이진수열과 그 깊이를 반환하는 함수
# 예 : 8을 입력받은 경우 1000이 아닌 0001000을 반환한다.
# 포화이진트리의 경우 원소 수가 2^1 - 1, 2^2 - 1, 2^3 - 1이어야 하기 때문
def bin_tree(number):                       
    i = 1                                   # 트리의 깊이
    while True:                             # 깊이 i인 트리에 number를 2진 형태로 모두 저장할 수 있으면
        if 2 ** (2 ** i - 1) - 1 >= number:
            break                           # 종료
        i += 1                              # 저장할 수 없으면 깊이 1 증가
    ans = ''                                # 2진수를 저장할 문자열
    while number > 0:                       # 2진수 구하기
        ans += str(number % 2)
        number //= 2
    n = len(ans)                            # 빈 트리를 0으로 채우는 과정
    while n < 2 ** i - 1:                   
        ans += '0'
        n += 1
    return ans[::-1], i                     # 2진수열과 깊이를 반환


def postorder(bins, p, f):                  # bins : 포화이진수열, p : 현재 노드, f : 현재 노드에서 탐색할 범위
    if f > 1:
        f //= 2
        a = postorder(bins, p - f, f)
        b = postorder(bins, p + f, f)
        if a == -1 or b == -1:              # 자식 노드에서 불가하다고 전달받은 경우
            return -1                       # 이 함수는 실행 불가
        if a + b != 0:                      # 자식 노드가 있는데
            if bins[p] == '0':              # 부모 노드가 없으면
                return -1                   # 불가 반환
            else:                           # 있으면
                return 1                    # 가능 반환
        else:                               # 자식 노드가 없으면
            if bins[p] == '0':              # 현재 노드 유무 반환
                return 0
            else:
                return 1
    else:                                   # 말단 노드의 원소 유무 반환
        if bins[p] == '0':                  
            return 0
        else:
            return 1


def solution(numbers):
    answer = []
    for number in numbers:
        answ, depth = bin_tree(number)
        # 포화이진트리의 경우 루트 노드는 2^(깊이-1) - 1을 인덱스로 가짐
        result = postorder(answ, 2 ** (depth - 1) - 1, 2 ** (depth - 1))
        result = 0 if result < 1 else 1
        answer.append(result)
    return answer
