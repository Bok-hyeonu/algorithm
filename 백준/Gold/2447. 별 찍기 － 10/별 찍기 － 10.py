# 2447. 별 찍기 - 10

# 규칙 0. 입력 N에 대해 3줄로 구분할 수 있다.
# 규칙 1. 1번 줄은 다 찍는다. 
# 규칙 2. 2번 줄은 가운데를 비운다.
# 규칙 3. 3번 줄은 다 찍는다.

def makestars(n):
    # 3의 0승인 경우 '*' 반환
    if n==1:
        return ['*']

    # 자신보다 한 급수 낮은 그림 가져오기(자신의 1/9사이즈)
    stars = makestars(n//3)
    L = []    # 각 줄의 정보를 저장할 내역
    # 첫 번째 줄(다 찍는다)
    for star in stars:
        L.append(star*3)
    # 두 번째 줄(가운데를 비운다(n//3))
    for star in stars:
        L.append(star+' '*(n//3)+star)
    # 세 번째 줄(다 찍는다)
    for star in stars:
        L.append(star*3)
    # 최종 결과 반환
    return L

N = int(input())                # 숫자
print('\n'.join(makestars(N)))  # 출력