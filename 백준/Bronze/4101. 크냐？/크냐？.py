
while True:
    front, back = map(int, input().split())
    if front == 0 and back == 0:
        break
    if front > back:
        print('Yes')
    else:
        print('No')
        