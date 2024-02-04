# 5597 / B5 / 과제 안 내신 분
st_list = list(range(1, 31)) # 학생 명단
for _ in range(28):
    n = int(input()) # 제출한 학생의 출석번호
    st_list[n-1] = 0 # 제출
for i in range(30):
    if st_list[i] == 0: # 제출학생이면
        pass # 통과
    else: # 미제출이면
        print(st_list[i]) # 번호 출력