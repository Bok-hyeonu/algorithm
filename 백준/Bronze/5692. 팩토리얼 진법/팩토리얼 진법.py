import sys
facts = [1, 2, 6, 24, 120]
while True:
  num = list(sys.stdin.readline().rstrip())
  if num[0] == '0':
    break
  result = 0
  for i in range(len(num)):
    result += int(num[i])*facts[len(num) - i - 1]
  sys.stdout.write(f'{result}\n')