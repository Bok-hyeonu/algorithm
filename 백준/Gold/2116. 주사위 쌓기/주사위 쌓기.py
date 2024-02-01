def high_low(dice, idx):
    if idx == 0:
        return max(dice[1:5]), dice[5]
    elif idx == 1:
        return max(dice[0], dice[2], dice[4], dice[5]), dice[3]
    elif idx == 2:
        return max(dice[0], dice[1], dice[3], dice[5]), dice[4]
    elif idx == 3:
        return max(dice[0], dice[2], dice[4], dice[5]), dice[1]
    elif idx == 4:
        return max(dice[0], dice[1], dice[3], dice[5]), dice[2]
    else:
        return max(dice[1:5]), dice[0]

cnt = int(input())

dice = list(map(int, input().split()))
high_a, high_b, high_c, high_d, high_e, high_f = dice
sum_a = max(dice[1:5])
sum_b = max(dice[0],dice[2], dice[4], dice[5])
sum_c = max(dice[0],dice[1], dice[3], dice[5])
sum_d = max(dice[0],dice[2], dice[4], dice[5])
sum_e = max(dice[0],dice[1], dice[3], dice[5])
sum_f = max(dice[1:5])
while cnt > 1:
    dice = list(map(int, input().split()))
    idx_a = dice.index(high_a)
    idx_b = dice.index(high_b)
    idx_c = dice.index(high_c)
    idx_d = dice.index(high_d)
    idx_e = dice.index(high_e)
    idx_f = dice.index(high_f)
    max_a, high_a = high_low(dice, idx_a)
    max_b, high_b = high_low(dice, idx_b)
    max_c, high_c = high_low(dice, idx_c)
    max_d, high_d = high_low(dice, idx_d)
    max_e, high_e = high_low(dice, idx_e)
    max_f, high_f = high_low(dice, idx_f)
    sum_a += max_a
    sum_b += max_b
    sum_c += max_c
    sum_d += max_d
    sum_e += max_e
    sum_f += max_f
    cnt -= 1

print(max(sum_a, sum_b, sum_c, sum_d, sum_e, sum_f))