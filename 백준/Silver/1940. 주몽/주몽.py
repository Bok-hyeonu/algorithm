# 1940 주몽

# 1. 재료들의 번호를 오름차순으로 정렬
# 2. 양 끝에서부터 좌측 포인터는 우측으로 우측 포인터는 좌측으로 움직이면서
# 3. 두 포인터가 가리키는 값의 합이 M과 같으면 개수 1 증가
# 4. 아닌 경우 조건에 맞추어 이동

N = int(input()) # 재료의 수
M = int(input()) # 갑옷을 만드는 데 드는 번호

materials = list(map(int, input().split())) # 재료들
materials.sort() # 재료들의 번호를 오름차순 정렬
l = 0       # 좌측 포인터
r = N-1     # 우측 포인터
cnt = 0     # 만들어진 갑옷의 개수
while l < r: # 두 포인터가 만나기 전까지
    # 재료 두 개의 합이 같으면 개수 1 증가, 두 포인터 모두 이동
    if materials[l] + materials[r] == M:
        cnt += 1
        l += 1
        r -= 1
    # 왼쪽 포인터가 가리키는 값이 오른쪽 포인터가 가리키는 값보다 중앙에 가까우면
    # 우측 포인터만 이동
    elif materials[l] > M - materials[r]:
        r -= 1
    # 오른쪽 포인터가 가리키는 값이 더 가까우면 우측 포인터 이동
    else:
        l += 1
print(cnt)  # 개수 출력