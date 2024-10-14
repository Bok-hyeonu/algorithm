# 1의 자리. 1*9*(10)^0
# 10의 자리. 2*9*(10)^1
# 100의 자리. 3*900


N = int(input())
nums = list(str(N))

length = 0
# 해당 자릿수 아래까지 더하기
for i in range(len(nums) - 1):
    length += 9*(i + 1)*(10 ** i)

# 남은 자릿수 더하기
length += (N - 10**(len(nums) - 1) + 1)*(len(nums))
print(length)
