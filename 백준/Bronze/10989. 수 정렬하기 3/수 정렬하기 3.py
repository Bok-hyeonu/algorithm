import sys
count = [0] * 10001 # 정렬을 위한 리스트
N = int(sys.stdin.readline().rstrip()) # N : 정렬할 수의 개수
# 수를 입력 받아 해당 수를 인덱스로 하는 값을 증가시킨다. 
for _ in range(N):
    count[int(sys.stdin.readline().rstrip())] += 1

# 처음부터 count 변수를 하나씩 순회하며 
# 해당 인덱스의 값만큼 출력을 진행한다.
# sys.stdout f-string을 이용하면 출력을 빠르게 진행할 수 있다.
for i in range(10001):
    for _ in range(count[i]):
        sys.stdout.write(f'{i}\n')