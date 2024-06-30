# 
N = int(input()) # 참가자의 수
# 사이즈별 신청자의 수
sizes = list(map(int, input().split()))
T, P = map(int, input().split()) # 옷 묶음, 펜

cnt = 0
for size in sizes:
    cnt += size//T
    if size % T != 0: cnt += 1

print(cnt)
print(N//P, N%P)