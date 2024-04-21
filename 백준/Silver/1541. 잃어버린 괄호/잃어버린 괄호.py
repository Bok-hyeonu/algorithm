# 1541 잃어버린 괄호

# 1. 최소가 되기 위해서는 빼기 기준으로 분할한 후 그것을 계속해서 빼 나가야 한다.

blocks = list(map(str, input().split('-'))) # '-' 기준 분할
result = 0 # 수식의 결과

for i in range(len(blocks)): # 블럭의 수만큼 반복
    # 블록을 더하기 기준으로 숫자로 분할
    numbers = list(map(int, blocks[i].split('+')))
    # 첫 번째 블록만 +
    if i == 0:
        result += sum(numbers)
    # 나머지 블록은 -
    else:
        result -= sum(numbers)

print(result) # 결과 출력