# E: 1-15 / S: 1-28 / M: 1-19

# 입력받기
E, S, M = map(int, input().split())
year = 1

while True:
    if ((year-E) % 15 == 0) and ((year-S) % 28 == 0) and ((year-M) % 19 == 0):
        break
    # if 문에 해당하지 않을 때는 year에 1을 더해준다
    year += 1

# 결과값 출력
print(year)