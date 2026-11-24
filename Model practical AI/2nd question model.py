import random
import math

N = 4
board = [random.randint(0, N-1) for _ in range(N)]

def conflicts(b):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if b[i] == b[j] or abs(b[i]-b[j]) == j-i:
                count += 1
    return count

T = 100

while T > 0.1:
    new = board.copy()
    col = random.randint(0, N-1)
    new[col] = random.randint(0, N-1)

    delta = conflicts(board) - conflicts(new)

    if delta > 0 or random.random() < math.exp(delta/T):
        board = new

    T *= 0.99

print("Final Board:")
for r in range(N):
    for c in range(N):
        print("Q" if board[c] == r else ".", end=" ")
    print()

print("Conflicts:", conflicts(board))
