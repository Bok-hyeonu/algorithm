S = input()

if len(S) == 1:
    print(0)
else:
    one = 0
    zero = 0
    prev = S[0]
    if prev == '1':
        one += 1
    else:
        zero += 1
    for i in range(1, len(S)):
        if prev != S[i]:
            prev = S[i]
            if prev == '0':
                zero += 1
            else:
                one += 1
    if one > zero:
        print(zero)
    else:
        print(one)