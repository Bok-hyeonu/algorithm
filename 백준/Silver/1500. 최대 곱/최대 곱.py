# 1500. 최대 곱

# 1. K개 수의 합이 S이면서 곱을 최대가 되게 하려면 
# 2. K개 수의 편차가 가장 작아야 한다. 합-차 공식에 의거 편차가 커질 수록 값이 작아진다
# 3. S를 K개 수로 나눈 몫과 나머지를 이용하여 K개 수의 값을 결정한다
# 4. 그 후 K개 수를 모두 곱한다.

S, K = map(int, input().split())

base = S // K       # 몫
reminder = S % K    # 나머지

nums = [base for _ in range(K)] # 몫을 K개 수에 배정
for i in range(reminder):       # 나머지 수만큼 +1
    nums[i] += 1

total = 1
for i in range(K):              # K개 수를 곱함
    total *= nums[i]

print(total)