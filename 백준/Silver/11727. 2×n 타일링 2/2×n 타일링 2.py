# n이 홀수인 경우 f(n) = 2*f(n-1) - 1
# n이 짝수인 경우 f(n) = 2*f(n-1) + 1의 점화식을 따름
# 다른 이유는 홀수에서 짝수가 되는 경우 1이 증가하게 됨으로써 전부 2인 경우의 수가 추가
# 짝수에서 홀수가 되는 경우는 추가 X. 모두 1로만 이뤄진 경우는 중복되므로 -1

n = int(input())
tiles = [0]*(n)
tiles[0] =  1
for i in range(1, n):
    if i % 2 == 0: # n이 홀수인 경우
        tiles[i] = 2*tiles[i-1] - 1
    else:
        tiles[i] = 2*tiles[i-1] + 1
print(tiles[n-1]%10007)