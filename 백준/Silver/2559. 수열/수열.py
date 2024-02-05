N, K = map(int, input().split())
temp_list = list(map(int, input().split()))
total = hap = sum(temp_list[:K])
for i in range(1, N-K+1):
    hap -= temp_list[i-1]
    hap += temp_list[i+K-1]
    if hap > total:
        total = hap

print(total)