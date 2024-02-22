code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
T = int(input()) 
for tc in range(1, T+1):
    # N : 세로, M : 가로
    N, M = map(int, input().split())
    # 배열 입력
    arr = [input().strip() for _ in range(N)]
    password = []
    end = -1
 
    for bits in arr: # 한 줄마다
        if int(bits): # 정수로 변환
 
            while bits[end] != '1': # 배열의 마지막이 1이 나올때까지
                end -= 1            # 한 칸 땡김? 밈?
            password = bits[end + 1 - 56:end + 1] # 그 지점에서부터 뒤로 56칸 추출
            break # 종료
 
    pass_code = [code[password[i*7:(i+1)*7]] for i in range(8)] # 8칸 단위로 분해
    result = sum(pass_code)                                     # 딕셔너리에서 값을 찾아 더함
    is_valid = sum(pass_code[0::2]) * 3 + sum(pass_code[1::2])  # 홀수 칸 * 3, 짝수 칸 그냥 더하기
 
    if is_valid % 10 == 0:              # 10으로 나눠진다면
        print(f'#{tc}', result)         # 암호 출력
    else:                               # 안 나눠지면
        print(f'#{tc}', 0)              # 암호가 아님