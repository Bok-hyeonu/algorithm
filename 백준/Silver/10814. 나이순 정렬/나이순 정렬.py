import sys
infos = [[] for _ in range(201)]            # 200살까지의 정보를 담을 이중 배열
N = int(input())                            # 입력값의 수
for i in range(N):                          # N쌍을 입력 받음
    info = sys.stdin.readline().split()
    infos[int(info[0])].append(info[1])     # 나이를 인덱스로 하는 이중 배열에 정보 저장

for i in range(1, 201):                     # 1살부터 200살까지
    for info in infos[i]:                   # 있는 정보를 모두 출력
        sys.stdout.write(f"{i} {info}\n")