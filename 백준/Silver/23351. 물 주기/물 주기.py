# 23351. 물 주기

N, K, A, B = map(int, input().split())
day = 0

arr = [K] * N
loca = 0

while 0 not in arr:
    loca = arr.index(min(arr))
    for i in range(A):
        arr[loca + i] += B

    for i in range(N):
        arr[i] -= 1

    day += 1

print(day)