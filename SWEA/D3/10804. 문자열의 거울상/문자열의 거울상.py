T = int(input())
mirror_dict = {'b':'d', 'd':'b', 'p':'q', 'q':'p'} # 키가 거울에 비쳐줬을 때의 값
for tc in range(1, T + 1):
    string = input() # 문자열
    # 문자열을 순회하며 거울에 비춘 값을 저장
    str_list = [mirror_dict[chr] for chr in string] 
    # join 메서드를 이용하여 뒤집은 리스트를 합쳐서 하나의 문자열로 만들어 출력
    result = ''.join(reversed(str_list))
    print(f'#{tc}', result)