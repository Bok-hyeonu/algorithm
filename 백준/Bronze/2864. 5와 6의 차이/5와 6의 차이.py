# 2864. 5와 6의 차이

A, B = input().split()
minA = list(A)
minB = list(B)
maxA = list(A)
maxB = list(B)

def changeNum(lst, bef, aft):
    for i in range(len(lst)):
        if lst[i] == bef:
            lst[i] = aft
    
    return int(''.join(lst))

amin = changeNum(minA, '6', '5')
bmin = changeNum(minB, '6', '5')
amax = changeNum(maxA, '5', '6')
bmax = changeNum(maxB, '5', '6')

print(amin + bmin, amax + bmax)