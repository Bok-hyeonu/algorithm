n = int(input())
if n == 1:
    print(1)
else:
    tiles = [0]*(n+1)
    tiles[0] = tiles[1] = 1
    for i in range(2, n+1):
        tiles[i] = tiles[i-1] + tiles[i-2]
    print(tiles[n]%10007)