import sys
# 1. 장대 3에 위치한 원반은 기존의 하노이탑 규칙을 따른다.
# 2. 즉, 원판의 반경이 큰 원판이 작은 원판보다 무조건 아래 있어야 한다.
# 3. 따라서, 원판 크기 내림차순으로 장대 3에 쌓는다.
# 4. 장대 1과 장대 2 중에서 장대 3에 위치시켜야 할 원판을 찾을 때까지
# 하나의 장대에서 다른 장대로 옮긴다.
# 5. 장대 3에 위치시킬 원판을 찾은 경우 해당 장대에서 장대 3으로 원판을 옮긴다.
# 6. 장대 3에 위치시킬 원판이 어딨는지 찾기 위해 최초에 원판이 쌓인 순서를 저장해놓는다.

N = int(sys.stdin.readline())
st1 = list(map(int, sys.stdin.readline().split())) # 장대 1

# 최초 원판이 쌓인 순서 저장
idxs = [0]*(N) 
for i in range(N):
    idxs[st1[i]-1] = i
top1 = N-1  # 장대 1은 포화 상태

st2 = [0]*N # 장대 2
top2 = -1
bot = N # 장대 3에 쌓아야 하는 원판
now = N # 장대 1과 장대 2를 구분 짓는 위치
cnt = 0 # 원판의 이동 횟수

result = '' # 이동 내역

while bot > 0: # 원판이 남아있을 때까지
    # 찾으려는 원판의 장대 위치 탐색
    if idxs[bot-1] < now: 
        tar = 1
    else:
        tar = 2 
    now = idxs[bot-1]
    # bot의 위치에 따라 진행    
    if tar == 1: # bot가 장대 1에 있으면
        # bot가 나올 때까지 장대 1에서 pop해서 장대 2에 push
        while st1[top1] != bot:
            top2 += 1  
            st2[top2] = st1[top1]   # pop & push
            top1 -= 1
            cnt += 1                # 이동횟수 증가
            result += '1 2\n'       # 1번 장대에서 2번 장대로
            
        top1 -= 1           # bot를 pop
        result += '1 3\n'   # 1번 장대에서 3번 장대로
        cnt += 1            # 이동횟수 증가
        
    else:                   # bot가 장대 2에 있으면
        # bot가 나올 때까지 장대 2에서 pop해서 장대 1에 push
        while st2[top2] != bot:
            top1 += 1
            st1[top1] = st2[top2]   # pop & push
            top2 -= 1
            cnt += 1                # 이동횟수 증가
            result += '2 1\n'       # 2번 장대에서 1번 장대로

        top2 -= 1           # bot를 pop
        result += '2 3\n'   # 2번 장대에서 3번 장대로
        cnt += 1            # 이동횟수 증가
        
    bot -= 1 # 장대 3에 쌓아야 하는 원판 번호 1 감소
    
sys.stdout.write(f'{cnt}\n')    # 이동 횟수
sys.stdout.write(f'{result}')   # 이동 내역