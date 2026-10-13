from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = set(word1 + word2 + result)

for perm in permutations(range(10), len(letters)):
    d = dict(zip(letters, perm))

    if d[word1[0]] == 0 or d[word2[0]] == 0 or d[result[0]] == 0:
        continue

    a = int(''.join(str(d[c]) for c in word1))
    b = int(''.join(str(d[c]) for c in word2))
    c = int(''.join(str(d[x]) for x in result))

    if a + b == c:
        print(a, "+", b, "=", c)
        break
