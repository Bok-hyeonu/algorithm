# 25304 / 영수증 / B4
X = int(input()) # 총 금액
N = int(input()) # 물건의 종류의 수
while N > 0:
    a, b = map(int, input().split()) # 물건의 단가, 개수
    X -= a*b # 단가와 값을 곱한 것을 총 금액에서 뺌
    N -= 1 # 다음 물건

if X == 0: # 물건 값의 합과 총 금액이 일치하면 
    print('Yes') # Yes 출력
else: # 일치하지 않으면
    print('No') # No 출력