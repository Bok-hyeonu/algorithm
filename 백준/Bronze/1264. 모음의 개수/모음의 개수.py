while True:
    inputs = input()
    if inputs == '#':
        break
    inputs = inputs.lower()
    cnt = 0
    for i in inputs:
        if i in ('a', 'e', 'i', 'o', 'u'):
            cnt += 1
    print(cnt)