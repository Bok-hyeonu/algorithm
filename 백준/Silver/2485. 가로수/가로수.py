# 가로수의 수가 최소가 되기 위해서는
# 간격이 최대가 되어야 한다.
# 가로수 간 간격이 최대가 되게 하기 위해서는 각 간격의 최대 공약수를 구하면 된다.
import sys
N = int(sys.stdin.readline())
num0 = int(sys.stdin.readline())        # 첫 번째 가로수
num1 = int(sys.stdin.readline())        # 두 번째 가로수
pre_int = num1 - num0                   # 현재까지 가능한 최대 간격
for _ in range(N-2):
    num = int(sys.stdin.readline())     # 현재 가로수의 위치
    now_int = num - num1                # 현재 간격(현재 가로수에서 이전 가로수를 빼서 구한다.)
    while now_int%pre_int != 0:          # 간격의 최대 공약수
        now_int, pre_int = pre_int, now_int%pre_int
    num1 = num 
    
# 간격을 구했다면 해당 간격대로 가로수를 심었을 때의 가로수 수에서
# 현재 가로수 수 N개를 뺀다.
# 심은 후의 총 가로수 수 : (끝 - 시작)/간격 + 1
result = (num1 - num0)//pre_int + 1 - N
print(result)