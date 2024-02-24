import sys

N, M = map(int, sys.stdin.readline().split()) # N : 저장된 사이트의 수, M : 찾으려는 사이트의 수
pw_dict = dict() # 저장하려는 딕셔너리
for _ in range(N): # 저장
    pws = sys.stdin.readline().split()
    pw_dict[pws[0]] = pws[1]
for _ in range(M): # 출력
    sys.stdout.write(f'{pw_dict[sys.stdin.readline().rstrip()]}\n')