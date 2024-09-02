# 23971. ZOAC 4

H, W, N, M = map(int, input().split())

sangha = H // (N+1)
jwaoo = W // (M+1)
if H % (N+1):
    sangha += 1

if W % (M+1):
    jwaoo += 1

print(sangha * jwaoo)