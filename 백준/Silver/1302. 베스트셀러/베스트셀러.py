import sys
input = sys.stdin.readline

N = int(input())
books = dict()
for _ in range(N):
    book = input()
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1

names = list(books.keys())
names.sort()

bestseller = names[0]
bestcnt = books[bestseller]

for book in names:
    if books[book] > bestcnt:
        bestcnt = books[book]
        bestseller = book

print(bestseller)