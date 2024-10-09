L = int(input())                    # 집합의 길이
S = list(map(int, input().split())) # 집합
n = int(input())                    # 포함해야 하는 수

S.sort()

if n in S:
  print(0)
else:
    min = 0
    max = 0
    for num in S:            # 배열중에서 n과 가장 근접한 두 수를 구한다.
        if num < n:     
            min = num
        elif num > n and max == 0:
            max = num
    max -= 1                    # 1과 7사이에 n이 2이면 1과 7은 제외
    min += 1
    # n보다 작은 수와 만족할 경우 + n보다 큰 수와 만족할 경우
    print((n-min)*(max-n+1) + (max-n))

