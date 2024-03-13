# 카운팅 정렬을 이용해 풀이합니다.
import sys

N = int(sys.stdin.readline()) # 수의 개수
arr = [0]*8001 # -4000부터 4000까지의 값의 개수를 저장할 배열

# 입력을 받을때마다 해당하는 수의 개수를 증가
for _ in range(N):
    arr[int(sys.stdin.readline())+4000] += 1
    
# 1. 산술평균(전체 합의 평균)
total = 0
for i in range(8001):
    total += (i-4000)*arr[i]
sys.stdout.write(f'{round(total/N)}\n')

# 2. 중앙값
# N이 홀수인 경우 중앙값은 (N+1)//2
target = (N+1)//2           # target번째 값이 중앙값
mid = 0                     # 처음으로 값의 개수가 target 이상이 되는 값이 중앙값
for i in range(8001):
    mid += arr[i]
    if mid >= target: 
        med = i-4000
        break
sys.stdout.write(f'{med}\n')

# 3. 최빈값
mod = -1                    # 최빈값의 수
mod_val = -4001             # 최빈값의 값
mods = []
for i in range(8001):
    if arr[i] == mod:       # 최빈값의 개수가 같은 경우
        mods.append(i-4000)
    elif arr[i] > mod:      # 현재까지 최빈값의 개수보다 많은 경우
        mods = [i-4000]     # 새로운 최빈값 리스트 생성
        mod = arr[i]        # 최빈값의 수 갱신

if len(mods) == 1:          # 최빈값이 하나인 경우
    sys.stdout.write(f'{mods[0]}\n')
else:                       # 두 개 이상인 경우 두 번째로 작은 값 출력
    sys.stdout.write(f'{mods[1]}\n')

# 4. 범위
# 값이 첫 번째로 등장하는 경우가 범위의 좌측 끝
for i in range(8001):
    if arr[i] > 0:
        st = i
        break

# 값이 마지막으로 등장하는 경우가 범위의 우측 끝
ed = st
for i in range(st+1, 8001):
    if arr[i] > 0:
        ed = i

sys.stdout.write(f'{ed-st}\n')