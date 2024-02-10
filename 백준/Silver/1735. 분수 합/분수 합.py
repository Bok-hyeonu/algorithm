# 최소공배수법을 통해 도출된 분수가 기약분수가 맞는지에 대해 확인하는 것에 유의
A1, B1 = map(int, input().split()) # 첫 번째 분자 분모
A2, B2 = map(int, input().split()) # 두 번째 분자 분모

m1, m2 = B1, B2
while B1%B2!=0:
    B1, B2 = B2, B1%B2
lcm = m1*m2//B2 # 최소 공배수

c3 = res_c = A1*(lcm//m1)+A2*(lcm//m2) # 최소공배수법의 분자
m3 = res_m = lcm # 분모

while c3%m3!=0: # 기약분수가 맞는지 확인
    c3, m3 = m3, c3%m3 # 아니라면 기약분수화하기 위한 최대공약수 구함

print(res_c//m3, res_m//m3) # 최종 출력