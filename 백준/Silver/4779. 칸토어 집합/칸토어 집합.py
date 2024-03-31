while True:
    try:
        str = '-'
        n = int(input())
        for i in range(n):
            str = ((str + ' ' * len(str)) * 2).strip()
        print(str)
    except:
        break