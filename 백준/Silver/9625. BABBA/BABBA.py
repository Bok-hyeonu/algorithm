K = int(input())

DPB = [0]*(K+1)
DPA = [0]*(K+1)
DPA[0] = 1
DPB[1] = 1

for i in range(2, K+1):
    DPB[i] = DPB[i - 1] + DPB[i-2]
    DPA[i] = DPA[i - 1] + DPA[i-2]

print(DPA[K], DPB[K])