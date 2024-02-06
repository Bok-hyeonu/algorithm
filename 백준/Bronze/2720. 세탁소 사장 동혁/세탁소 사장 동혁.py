T = int(input())
for tc in range(1, T + 1):
    buck = int(input()) # 거스름돈
    quar = buck//25 # 쿼터의 수
    buck %= 25 # 쿼터 준 나머지
    dime = buck//10 # 다임의 수
    buck %= 10 # 다임 준 나머지
    nike = buck//5 # 니켈의 수
    buck %= 5 # 니켈 준 나머지(페니)
    print(quar, dime, nike, buck) # 출력