# 2018 수들의 합 5

N = int(input())

cnt = 1         # 연속된 수들의 합으로 나타낼 수 있는 갯수(자기 자신 포함)
st, ed = 1, 1   # 투 포인터
tot = 1         # 연속된 수의 합

# 종료 조건까지
while ed != N:
    # 합이 N이면
    if tot == N:
        # 개수 증가 및 ed 포인터 이동
        cnt += 1
        ed += 1
        tot += ed
    # N보다 크면 st 포인터를 이동시키고 연속합 -
    elif tot > N:
        tot -= st
        st += 1
    # N보다 작으면 ed 포인터를 이동시키도 연속합 +
    else:
        ed += 1
        tot += ed

print(cnt)