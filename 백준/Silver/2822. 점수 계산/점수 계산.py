scores = [(int(input()), i) for i in range(1, 9)]
scores.sort(reverse = True)
total = 0
idxs = []
for i in range(5):
    total += scores[i][0]
    idxs.append(scores[i][1])

idxs.sort()
print(total)
print(*idxs)