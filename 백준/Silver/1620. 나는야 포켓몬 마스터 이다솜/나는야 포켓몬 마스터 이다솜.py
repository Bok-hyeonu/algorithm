import sys
N, M = map(int, sys.stdin.readline().split()) # N : 도감 포켓몬 수, M : 질문 수
mons = dict()                           # 포켓몬 도감

for i in range(1, N + 1):               # 입력받음  
    p = sys.stdin.readline().rstrip()
    mons[p.lower()] = i                 # 대문자를 소문자로한 것을 키로 하여 딕셔너리에 저장
    mons[str(i)] = p                    # 반대를 키로 하여 저장

for _ in range(M):                      # M회의 질문에 대해                      
    t = sys.stdin.readline().rstrip().lower()
    sys.stdout.write(f'{mons[t]}\n')    # 해당하는 결과를 출력