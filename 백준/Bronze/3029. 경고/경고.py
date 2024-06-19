start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))


def calcul(lst):
    return lst[0]*3600 + lst[1]*60 + lst[2]



def result(time):
    hour = time // 3600
    time %= 3600
    minute = time // 60
    time %= 60
    print(f'{hour:02d}:{minute:02d}:{time:02d}')

s = calcul(start)
e = calcul(end)


if e <= s:
    e += 86400

result(e-s)