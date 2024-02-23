from collections import deque
def is_valid(lst):
    if lst in visited:
        return 0
    elif (sum(list(lst)[::2])*3 + sum(list(lst)[1::2])) % 10 == 0:
        visited.append(lst)
        return sum(lst)
    else:
        return 0


code = {'0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9}
hex_to_bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
              '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
              'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110',
              'F': '1111'}

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())        # N, M
    arr = [input().strip() for _ in range(N)]
    str_lst = []                # 입력에서 중복 없이 0이 아닌 후보들을 저장할 리스트
    total = 0                   # 총합을 저장할 변수
    visited = []

    for e in arr:                   # 입력에서 중복 없이 0이 아닌 후보들을 저장
        if e != '0'*M and e not in str_lst:
            str_lst.append(e)

    for temp in str_lst:
        temp = temp.rstrip('0')     # 오른쪽의 0을 전부 삭제 (암호코드는 오른쪽이 전부 1로 끝남)

        str_bin = ''

        for h in temp:              # 문자열의 16진수를 2진수로 변환환
            str_bin += hex_to_bin[h]

        str_bin = str_bin.rstrip('0')     # 오른쪽의 0을 전부 삭제 (암호코드는 오른쪽이 전부 1로 끝남)

        while str_bin:      # 이진수 문자열이 완전 없어질 때까지 반복
            i = 1           # 암호코드 선 굵기

            while len(str_bin) >= 7*8*i:        # 암호코드가 존재 가능한 길이인 경우에 반복
                # 암호를 저장할 덱 생성
                pw = deque()
                # 원래 문자열을 건드리지 않고 임시 문자열 생성
                temp_str_bin = ''.join(str_bin[s] if (s+1)%i == 0 else '' for s in range(len(str_bin)))
                for _ in range(8):  # 암호 문자열 길이인 8만큼 반복
                    try:
                        # 오른쪽부터 7개 문자열을 잘라서 딕셔너리에서 암호를 찾고, 찾은 암호를 pw 덱의 왼쪽에 계속 추가해줌
                        pw.appendleft(code[temp_str_bin[-7:]])
                        temp_str_bin = temp_str_bin[:-7]
                    except KeyError:        # i 굵기의 암호코드를 찾지 못한 경우
                        i += 1              # 다음 굵기 탐색을 위해 +1
                        break
                if len(pw) == 8:
                    total += is_valid(pw)
                    str_bin = str_bin[:-7*8*i]
                    break
            str_bin = str_bin.rstrip('0')

    result = total
    print(f'#{tc}', result)