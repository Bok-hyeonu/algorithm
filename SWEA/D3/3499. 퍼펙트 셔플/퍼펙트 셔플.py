T = int(input())
for tc in range(1, T + 1):
    N= int(input())
    cards = list(input().split()) # 카드들
    print(f'#{tc}', end=' ')
    if N%2 == 0:
        cnt = N//2
    else:
        cnt = N//2 + 1
    for i in range(N//2):
        print(cards[i], end = ' ')
        print(cards[cnt+i], end = ' ')
    if N%2 == 1:
        print(cards[cnt-1], end = ' ')
    print()