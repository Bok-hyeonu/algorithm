# 1267. 핸드폰 요금

N = int(input())
usages = list(map(int, input().split()))    # 이용량

Youngsik = 0
Minsik = 0

for usage in usages:
    usage += 1
    Youngsik += (usage//30) * 10
    Minsik += (usage//60) * 15
    
    if usage % 30:
        Youngsik += 10
    
    if usage % 60:
        Minsik += 15

if Youngsik == Minsik:
    print(f'Y M {Youngsik}')
elif Youngsik > Minsik:
    print(f'M {Minsik}')
else:
    print(f'Y {Youngsik}')