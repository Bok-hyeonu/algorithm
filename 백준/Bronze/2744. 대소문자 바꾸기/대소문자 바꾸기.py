letters = input()
for letter in letters:
    if ord(letter) > 96:
        print(chr(ord(letter)-32), end='')
    else:
        print(chr(ord(letter)+32), end='')