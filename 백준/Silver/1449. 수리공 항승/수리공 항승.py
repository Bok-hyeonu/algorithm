# 1449. 수리공 항승

# 1. 물이 새는 곳을 오름차순 정렬한다.
# 2. 앞에서부터 테이프를 감아간다. 
# 3. 테이프를 감을 수 없는 경우 다음 테이프를 이용해 감는다.

N, L = map(int, input().split())    # 물이 새는 곳의 수, 테이프의 길이
leaks = list(map(int, input().split())) # 물이 새는 곳

leaks.sort()    # 물이 새는 곳 정렬

cnt = 1                     # 필요한 테이프의 수
st = leaks[0]               # 테이프를 감기 시작할 지점
for i in range(1, N):
    if leaks[i] - st < L:   # 미리 감은 테이프로 해결이 가능한 경우
        continue            # 다음 누수 지점으로 이동
    cnt += 1                # 사용할 테이프 추가
    st = leaks[i]           # 시작 지점 변경

print(cnt)