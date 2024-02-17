num = list(map(int, input())) # 입력을 리스트로 바꾸어 받는다.
num.sort(reverse=True) # reverse = True 옵션을 설정하여 내림차순 정렬을 진행한다.
num = list(map(str, num)) # 리스트의 정수 자료형인 원소를 문자열로 바꾸어준다.
print(''.join(num)) # join메서드를 사용하여 한 문자열로 출력한다.