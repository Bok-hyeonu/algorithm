
# 숫자가 무조건 하나는 들어옴
a = input()
b = input()
c = input()

# 셋 중 하나로부터 다음에 올 수를 구함
if c in ('FizzBuzz', 'Buzz', 'Fizz'):
    if b in ('FizzBuzz', 'Buzz', 'Fizz'):
        result = int(a) + 3
    else:
        result = int(b) + 2
else:
    result = int(c) + 1

# 해당 수가 FizzBuzz, Fizz, Buzz에 해당하는지 확인
if result % 15 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)